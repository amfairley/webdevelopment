from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class AnalyticsSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "analytics_home",
            "analytics_seo",
        ]

    def location(self, item):
        return reverse(item)