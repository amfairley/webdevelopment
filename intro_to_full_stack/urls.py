from django.urls import path
from . import views


urlpatterns = [
    path(
        'programming-and-the-web/',
        views.full_stack_programming_and_the_web,
        name="full_stack_programming_and_the_web"
    ),
    path(
        'github/',
        views.full_stack_github,
        name="full_stack_github"
    ),
]
