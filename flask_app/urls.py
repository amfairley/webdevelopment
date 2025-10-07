from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.flask_home, name="flask_home"),
    path('basics/', views.flask_basics, name="flask_basics"),
    path('database/', views.flask_database, name="flask_database"),
    path('template/', views.flask_template, name="flask_template"),
    path('create/', views.flask_create, name="flask_create"),
    path('read/', views.flask_read, name="flask_read"),
    path('update/', views.flask_update, name="flask_update"),
    path('delete/', views.flask_delete, name="flask_delete"),
]
