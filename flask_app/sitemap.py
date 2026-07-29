from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class FlaskSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "flask_home",
            "flask_basics",
            "flask_database",
            "flask_template",
            "flask_create",
            "flask_read",
            "flask_update",
            "flask_delete",
        ]

    def location(self, item):
        return reverse(item)