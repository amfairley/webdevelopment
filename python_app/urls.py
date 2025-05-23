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
]
