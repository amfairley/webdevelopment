from django.urls import path
from . import views


urlpatterns = [
    path(
        'programming_and_the_web/',
        views.full_stack_programming_and_the_web,
        name="full_stack_programming_and_the_web"
    ),
    path(
        'github/',
        views.full_stack_github,
        name="full_stack_github"
    ),
]
