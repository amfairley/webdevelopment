from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PythonSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "python_home",
            "python_variables",
            "python_data_types",
            "python_strings",
            "python_booleans",
            "python_lists",
            "python_tuples",
            "python_dictionaries",
            "python_sets",
            "python_regular_expressions",
            "python_functions",
            "python_input",
            "python_os",
            "python_math",
            "python_datetime",
            "python_pandas",
            "python_numpy",
            "python_csv",
            "python_json",
            "python_pillow",
            "python_scope",
            "python_loops",
            "python_conditionals",
            "python_classes",
            "python_unit_testing",
            "python_data_and_api_requests",
            "python_code_validation",
            "python_google_sheets_program",
        ]

    def location(self, item):
        return reverse(item)