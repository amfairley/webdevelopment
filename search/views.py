from django.shortcuts import render
from django.conf import settings
from algoliasearch.search.client import SearchClientSync

def search_view(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        try:
            # Initialize Algolia client with search-only API key
            client = SearchClientSync(settings.ALGOLIA_APP_ID, settings.ALGOLIA_SEARCH_KEY)

            # Perform the search
            res = client.search_single_index(
                "webdevgrad_pages",
                {
                    "query": query,
                }
            )

            # Get the hits (results)
            results = res.hits

        except Exception as e:
            # Optional: log error for debugging
            print("Algolia search error:", e)

    return render(request, "search/results.html", {
        "query": query,
        "results": results,
    })
