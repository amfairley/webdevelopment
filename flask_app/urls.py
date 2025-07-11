from django.urls import path
from . import views


urlpatterns = [
    path('', views.flask_home, name="flask_home"),
    path('basics/', views.flask_basics, name="flask_basics"),
    path('database/', views.flask_database, name="flask_database"),
    path('template/', views.flask_template, name="flask_template"),
]
