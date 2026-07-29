from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class DjangoSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "django_home",
            "django_getting_started_with_django",
            "django_admin",
            "django_settings",
            "django_urls",
            "django_apps",
            "django_templates",
            "django_views",
            "django_models",
            "django_forms",
            "django_templating_language",
            "django_error_pages",
            "django_crud",
            "django_messages",
            "django_static",
            "django_testing",
            "django_allauth",
            "django_search",
            "django_languages",
            "django_envpy",
        ]

    def location(self, item):
        return reverse(item)