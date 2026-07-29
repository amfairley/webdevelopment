from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ExamplesSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "examples",
        ]

    def location(self, item):
        return reverse(item)