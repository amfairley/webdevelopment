from django.urls import path
from . import views


urlpatterns = [
    path('', views.analytics_home, name="analytics_home"),
    path('SEO/', views.analytics_seo, name="analytics_seo"),
]
