from django.urls import path
from . import views


urlpatterns = [
    path('', views.backend_home, name="backend_home"),
    path('databases/', views.backend_databases, name="backend_databases"),
    path(
        'designing_a_database/',
        views.backend_designing_a_database,
        name="backend_designing_a_database"
    ),
]
