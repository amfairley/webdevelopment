import os
import sys
import django
from pathlib import Path

# Define route directory
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webdevelopment.settings")  # replace with your actual project.settings module
django.setup()


from bs4 import BeautifulSoup
from algoliasearch.search.client import SearchClient
from django.conf import settings
import asyncio
import re


# --- helper to slugify titles for anchor IDs ---
def slugify(value: str) -> str:
    """
    Converts a string into a slug suitable for use as an HTML element ID.
    Replaces all non-alphanumeric characters with hyphens, trims extras,
    and lowercases the result.
    """
    value = re.sub(r'[^a-zA-Z0-9]+', '-', value).strip('-')
    return value.lower()


async def run():
    """
    Reads all HTML templates in multiple folders across your project,
    extracts titles and paragraphs, clears the Algolia index, and uploads them.
    """

    print("Starting indexer...")

    # 1. Create Algolia client using your app ID and WRITE key
    client = SearchClient(settings.ALGOLIA_APP_ID, settings.ALGOLIA_WRITE_KEY)
    print("Algolia client initialized.")

    # 2. Choose the index
    index_name = 'webdevgrad_pages'
    print(f"Index '{index_name}' selected.")

    # --- CLEAR THE INDEX BEFORE UPLOADING NEW RECORDS ---
    print("Clearing existing records in the index...")
    response = await client.clear_objects(index_name)
    print(f"Clear index response: {response}")
    # ------------------------------------------------------

    # 3. List all template folders
    templates_dirs = [
        # Path(settings.BASE_DIR) / 'templates',             # main templates folder
        Path(settings.BASE_DIR) / 'HTML' / 'templates',    # app1 templates
        Path(settings.BASE_DIR) / 'intro_to_full_stack' / 'templates',    # app2 templates
        Path(settings.BASE_DIR) / 'CSS' / 'templates',
        Path(settings.BASE_DIR) / 'javascript_app' / 'templates',
        Path(settings.BASE_DIR) / 'python_app' / 'templates',
        Path(settings.BASE_DIR) / 'analytics' / 'templates',
        Path(settings.BASE_DIR) / 'backend' / 'templates',
        Path(settings.BASE_DIR) / 'flask_app' / 'templates',
        Path(settings.BASE_DIR) / 'django_app' / 'templates',
    ]
    print(f"Templates directories to scan: {templates_dirs}")

    records = []
    object_id = 1

    # 4. Loop through each templates folder and index all HTML files found
    for templates_path in templates_dirs:
        if not templates_path.exists():
            print(f"Warning: templates directory {templates_path} does not exist, skipping.")
            continue

        for file_path in templates_path.rglob("*.html"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    html = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.string if soup.title else file_path.stem
            paragraphs = " ".join(p.get_text(strip=True) for p in soup.find_all("p"))
            
            ### ADDITION: collect h4 headings with IDs
            h4_headings = [
                {"id": h.get("id"), "text": h.get_text(strip=True)}
                for h in soup.find_all("h4")
                if h.get("id")
            ]

            # --- build URL with anchor ID ---
            relative_path = file_path.relative_to(templates_path)
            relative_dir = relative_path.parent

            # Get to topic URL from includes or includes/code_snippets etc
            if relative_dir.name in {
                "code_snippets",
                "code_examples",
                "tips",
                "troubleshooting",
                "html_css_example",
            }:
                original_section = relative_dir.name
                preserved_part = relative_dir.name.replace("_", "-")  # convert underscores to hyphens
                relative_dir = relative_dir.parent.parent
                relative_url = relative_dir.as_posix().replace("_", "-")

                if relative_url.endswith("home"):
                    relative_url = relative_url  # no slash for home pages
                else:
                    relative_url.rstrip("/") + "/"  # Ensure only 1 slash

                dir_slug = relative_dir.as_posix().replace("/", "-").replace("_", "-") + "-" + preserved_part
                if original_section == "code_snippets":
                    section_type = "Code Snippet"
                elif original_section == "code_examples":
                    section_type = "Code Example"
                elif original_section == "tips":
                    section_type = "Tip"
                elif original_section == "troubleshooting":
                    section_type = "Troubleshooting"
                elif original_section == "html_css_example":
                    section_type = "HTML and CSS example"

                element_id = f"{dir_slug}-{slugify(title)}"

                # Update with website name 
                url_local = f"http://127.0.0.1:8000/{relative_url}#{element_id}"
                url_heroku = f"https://webdevgrad-3277133ed051.herokuapp.com/{relative_url}#{element_id}"

            elif relative_dir.name == "includes":
                relative_dir = relative_dir.parent
                relative_url = relative_dir.as_posix().replace("_", "-")

                if relative_url.endswith("home"):
                    relative_url = relative_url  # no slash for home pages
                else:
                    relative_url.rstrip("/") + "/"  # Ensure only 1 slash
                dir_slug = relative_dir.as_posix().replace("/", "-").replace("_", "-")
                section_type = "Topic Section"

                element_id = f"{dir_slug}-{slugify(title)}"

                # Update with website name 
                url_local = f"http://127.0.0.1:8000/{relative_url}#{element_id}"
                url_heroku = f"https://webdevgrad-3277133ed051.herokuapp.com/{relative_url}#{element_id}"

            else:
                relative_url = relative_dir.as_posix().replace("_", "-")

                if relative_url.endswith("home"):
                    relative_url = relative_url  # no slash for home pages
                else:
                    relative_url.rstrip("/") + "/"  # Ensure only 1 slash
                dir_slug = relative_dir.as_posix().replace("/", "-").replace("_", "-")
                section_type = "Topic Page"
                element_id = "N/A"

                url_local = f"http://127.0.0.1:8000/{relative_url}"
                url_heroku = f"https://webdevgrad-3277133ed051.herokuapp.com/{relative_url}"

            section = "Other"  # default
            for templates_path in templates_dirs:
                try:
                    relative = file_path.relative_to(templates_path)
                    section = relative.parts[0]
                    break
                except ValueError:
                    continue

            # Capitalize if not HTML or CSS
            if section not in {"HTML", "CSS"}:
                section = section.title()

            # Rename JavaScript_App section
            if section == "Intro_To_Full_Stack":
                section = "Web Development"

            if section == "Javascript_App":
                section = "JavaScript"

            if section == "Python_App":
                section = "Python"

            if section == "Flask_App":
                section = "Flask"

            if section == "Django_App":
                section = "Django"

            # Ranking based on section type
            sort_order = {
                "Topic Page": 0,
                "Topic Section": 1,
                # Leave 2 for subsection
                "Troubleshooting": 3,
                "Code Example": 4,
                "HTML and CSS example": 5,
                "Code Snippet": 6,
                "Tip": 7,
            }
            rank_priority = sort_order.get(section_type, 99)

            pretty_title = title.replace("_", " ").replace("-", " ").title()
            # Special case for Home pages
            if pretty_title == "Home":
                pretty_title = f"{section} Home"

            # Update Pretty Title with Corrections
            pretty_title = pretty_title.replace("Html", "HTML")
            pretty_title = pretty_title.replace("Css", "CSS")
            pretty_title = pretty_title.replace("Javascript_App", "JavaScript")
            pretty_title = pretty_title.replace("Javascript", "JavaScript")
            pretty_title = pretty_title.replace("Js", "JS")
            pretty_title = pretty_title.replace("Python_App", "Python")
            pretty_title = pretty_title.replace("Flask_App", "Flask")
            pretty_title = pretty_title.replace("Django_App", "Django")

            # Update url from x-app to X
            url_local = url_local.replace("javascript-app", "JavaScript")
            url_heroku = url_heroku.replace("javascript-app", "JavaScript")
            url_local = url_local.replace("python-app", "Python")
            url_heroku = url_heroku.replace("python-app", "Python")
            url_local = url_local.replace("flask-app", "Flask")
            url_heroku = url_heroku.replace("flask-app", "Flask")
            url_local = url_local.replace("django-app", "Django")
            url_heroku = url_heroku.replace("django-app", "Django")

            # Add in extra keywords so that HTML returns HTML home
            extra_keywords = []
            if pretty_title.endswith("Home"):
                extra_keywords.append(section) 

            # Skip if the title is contents and append if it is not
            if title.lower() != "contents":
                records.append({
                    "objectID": object_id,
                    "file": str(file_path.relative_to(templates_path)),
                    "title": title,
                    "prettyTitle": pretty_title,
                    "elementID": element_id,
                    "sectionType": section_type,
                    "section": section,
                    "content": paragraphs,
                    "urlLocal": url_local,
                    "urlHeroku": url_heroku,
                    "rankPriority": rank_priority,
                    "keywords": extra_keywords,
                })
                print(f"Prepared record {object_id}: {title} ({file_path})")
                object_id += 1

                # Also index each h4 heading with ID
                for h in h4_headings:
                    heading_element_id = h["id"]
                    heading_url_local = f"{url_local.split('#')[0]}#{heading_element_id}"
                    heading_url_heroku = f"{url_heroku.split('#')[0]}#{heading_element_id}"

                    records.append({
                        "objectID": object_id,
                        "file": str(file_path.relative_to(templates_path)),
                        "title": h["text"],
                        "prettyTitle": h["text"],
                        "elementID": heading_element_id,
                        "sectionType": "Topic Subsection",
                        "section": section,
                        "content": "",
                        "urlLocal": heading_url_local,
                        "urlHeroku": heading_url_heroku,
                        "rankPriority": 2,
                        "keywords": [section],
                    })
                    print(f"Prepared subsection record {object_id}: {h['text']} ({file_path})")
                    object_id += 1
            else:
                print(f"Skipping file {file_path} because title is 'contents'")

    print(f"Total records prepared to upload: {len(records)}")

    # 5. Upload all records
    if records:
        print("Uploading records to Algolia...")
        upload_response = await client.save_objects(index_name, records)
        print(f"Upload response: {upload_response}")
    else:
        print("No records to upload.")

    await client.close()
    print("Algolia client closed. Indexing complete.")

if __name__ == "__main__":
    import asyncio
    print("Starting async indexer...")
    asyncio.run(run())