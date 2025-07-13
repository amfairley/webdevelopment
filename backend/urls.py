from django.urls import path
from . import views


urlpatterns = [
    path('', views.backend_home, name="backend_home"),
]
