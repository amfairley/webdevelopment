from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.analytics_home, name="analytics_home"),
    path('seo/', views.analytics_seo, name="analytics_seo"),
]
