from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class BackendSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "backend_home",
            "backend_databases",
            "backend_designing_a_database",
            "backend_sql",
            "backend_postgresql",
            "backend_orms",
            "backend_sqlalchemy",
        ]

    def location(self, item):
        return reverse(item)