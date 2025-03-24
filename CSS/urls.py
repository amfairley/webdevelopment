from django.urls import path
from . import views


urlpatterns = [
    path('', views.CSS_home, name="CSS_home"),
]
