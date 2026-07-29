from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class IntroSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "full_stack_programming_and_the_web",
            "full_stack_github",
            "full_stack_website_development",
            "full_stack_sizes",
            "full_stack_colour",
            "full_stack_project_goals",
            "full_stack_user_stories",
            "full_stack_five_stages",
            "full_stack_features",
            "full_stack_testing",
            "full_stack_google_dev_tools",
            "full_stack_readme",
            "full_stack_vscode",
            "full_stack_pseudocode",
        ]

    def location(self, item):
        return reverse(item)