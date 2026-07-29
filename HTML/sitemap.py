from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HTMLSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "HTML_home",
            "HTML_introducing_elements",
            "HTML_common_elements",
            "HTML_lists",
            "HTML_tables",
            "HTML_forms",
            "HTML_links",
            "HTML_media",
            "HTML_buttons",
            "HTML_semantic",
            "HTML_accessibility",
            "HTML_example",
        ]

    def location(self, item):
        return reverse(item)