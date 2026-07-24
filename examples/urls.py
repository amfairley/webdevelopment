from django.urls import path
from . import views


urlpatterns = [
    path('examples/', views.examples, name="examples"),
]
