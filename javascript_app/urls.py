from django.urls import path
from . import views


urlpatterns = [
    path('', views.JavaScript_home, name="JavaScript_home"),
]
