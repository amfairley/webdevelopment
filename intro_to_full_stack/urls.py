from django.urls import path
from . import views


urlpatterns = [
    path('', views.intro_to_full_stack, name="intro_to_full_stack"),
]
