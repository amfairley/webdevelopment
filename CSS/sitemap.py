from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class CSSSitemap(Sitemap):

    changefreq = "weekly"
    priority = 1

    def items(self):
        return [
            "CSS_home",
            "CSS_selectors",
            "CSS_box_model",
            "CSS_display_and_positioning",
            "CSS_flexbox",
            "CSS_grids",
            "CSS_backgrounds",
            "CSS_visibility_and_z_positioning",
            "CSS_cursor",
            "CSS_typography",
            "CSS_links_and_buttons",
            "CSS_lists",
            "CSS_forms",
            "CSS_transitions",
            "CSS_responsive_design",
            "CSS_bootstrap",
            "CSS_css_validation",
        ]

    def location(self, item):
        return reverse(item)