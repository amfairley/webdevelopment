from python_app.sitemap import PythonSitemap
from analytics.sitemap import AnalyticsSitemap
from backend.sitemap import BackendSitemap
from CSS.sitemap import CSSSitemap
from deployment.sitemap import DeploymentSitemap
from django_app.sitemap import DjangoSitemap
from examples.sitemap import ExamplesSitemap
from flask_app.sitemap import FlaskSitemap
from homepage.sitemap import HomepageSitemap
from HTML.sitemap import HTMLSitemap
from intro_to_full_stack.sitemap import IntroSitemap
from javascript_app.sitemap import JavaScriptSitemap

sitemaps = {
    "python": PythonSitemap,
    "analytics": AnalyticsSitemap,
    "backend": BackendSitemap,
    "css": CSSSitemap,
    "deployment": DeploymentSitemap,
    "django": DjangoSitemap,
    "examples": ExamplesSitemap,
    "flask": FlaskSitemap,
    "homepage": HomepageSitemap,
    'html': HTMLSitemap,
    'intro_to_full_stack': IntroSitemap,
    'javascript': JavaScriptSitemap,
}