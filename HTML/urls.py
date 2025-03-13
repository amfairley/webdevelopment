from django.urls import path
from . import views


urlpatterns = [
    path('', views.HTML_home, name="HTML_home"),
    path(
        'introducing_elements/',
        views.HTML_introducing_elements,
        name="HTML_introducing_elements"
    ),
    path(
        'common_elements/',
        views.HTML_common_elements,
        name="HTML_common_elements"
    ),
    path(
        'lists/',
        views.HTML_lists,
        name="HTML_lists"
    ),
    path(
        'tables/',
        views.HTML_tables,
        name="HTML_tables"
    )
]
