from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.python_home,
        name="python_home"
    ),
    path(
        'variables/',
        views.python_variables,
        name="python_variables"
    ),
    path(
        'data_types/',
        views.python_data_types,
        name="python_data_types"
    ),
    path(
        'strings/',
        views.python_strings,
        name="python_strings"
    ),
    path(
        'booleans/',
        views.python_booleans,
        name="python_booleans"
    ),
]
