from django.urls import path
from . import views


urlpatterns = [
    path('', views.JavaScript_home, name="JavaScript_home"),
    path(
        'variables/',
        views.JavaScript_variables,
        name="JavaScript_variables"
    ),
    path(
        'scope/',
        views.JavaScript_scope,
        name="JavaScript_scope"
    ),
    path(
        'data_types/',
        views.JavaScript_data_types,
        name="JavaScript_data_types"
    ),
]
