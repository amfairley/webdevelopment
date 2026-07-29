from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class JavaScriptSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "JavaScript_home",
            "JavaScript_variables",
            "JavaScript_scope",
            "JavaScript_data_types",
            "JavaScript_math",
            "JavaScript_arrays",
            "JavaScript_sets",
            "JavaScript_objects",
            "JavaScript_console_commands",
            "JavaScript_functions",
            "JavaScript_conditional_statements",
            "JavaScript_for_loops",
            "JavaScript_while_loops",
            "JavaScript_try",
            "JavaScript_nested_loops",
            "JavaScript_the_dom",
            "JavaScript_targeting_the_dom",
            "JavaScript_manipulating_the_dom",
            "JavaScript_events",
            "JavaScript_jquery",
            "JavaScript_debugging",
            "JavaScript_validation",
            "JavaScript_emailjs",
        ]

    def location(self, item):
        return reverse(item)