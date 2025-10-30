from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.deployment_home, name="deployment_home"),
]
