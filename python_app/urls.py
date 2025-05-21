from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.python_home,
        name="python_home"
    ),
]
