from django.urls import path
from . import views


urlpatterns = [
    path('', views.JavaScript_home, name="JavaScript_home"),
    path('variables/', views.JavaScript_variables, name="JavaScript_variables"),
]
