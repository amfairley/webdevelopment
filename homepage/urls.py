from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('example/', views.example, name="example")
]
