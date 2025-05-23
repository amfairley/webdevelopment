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
    path(
        'lists/',
        views.python_lists,
        name="python_lists"
    ),
    path(
        'tuples/',
        views.python_tuples,
        name="python_tuples"
    ),
    path(
        'dictionaries/',
        views.python_dictionaries,
        name="python_dictionaries"
    ),
    path(
        'sets/',
        views.python_sets,
        name="python_sets"
    ),
    path(
        'regular_expressions/',
        views.python_regular_expressions,
        name="python_regular_expressions"
    ),
]
