from django.urls import path
from . import views


urlpatterns = [
    path('', views.HTML_home, name="HTML_home"),
]
