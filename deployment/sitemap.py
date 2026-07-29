from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class DeploymentSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "deployment_home",
        ]

    def location(self, item):
        return reverse(item)