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
    path(
        'website-development/',
        views.full_stack_website_development,
        name="full_stack_website_development"
    ),
    path(
        'sizes/',
        views.full_stack_sizes,
        name="full_stack_sizes"
    ),
    path(
        'colour/',
        views.full_stack_colour,
        name="full_stack_colour"
    ),
]
