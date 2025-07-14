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
    path(
        'sql/',
        views.backend_sql,
        name="backend_sql"
    ),
    path(
        'postgresql/',
        views.backend_postgresql,
        name="backend_postgresql"
    ),
    path(
        'orms/',
        views.backend_orms,
        name="backend_orms"
    ),
    path(
        'sqlalchemy/',
        views.backend_sqlalchemy,
        name="backend_sqlalchemy"
    ),
]
