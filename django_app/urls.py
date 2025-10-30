from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.django_home, name="django_home"),
    path(
        'getting-started-with-django/',
        views.django_getting_started_with_django,
        name="django_getting_started_with_django"
    ),
    path('admin/', views.django_admin, name="django_admin"),
    path('settings/', views.django_settings, name="django_settings"),
    path('urls/', views.django_urls, name="django_urls"),
    path('apps/', views.django_apps, name="django_apps"),
    path('templates/', views.django_templates, name="django_templates"),
    path('views/', views.django_views, name="django_views"),
    path('models/', views.django_models, name="django_models"),
    path('forms/', views.django_forms, name="django_forms"),
    path('templating-language/', views.django_templating_language, name="django_templating_language"),
    path('error-pages/', views.django_error_pages, name="django_error_pages"),
    path('crud/', views.django_crud, name="django_crud"),
    path('messages/', views.django_messages, name="django_messages"),
    path('static/', views.django_static, name="django_static"),
    path('testing/', views.django_testing, name="django_testing"),
    path('allauth/', views.django_allauth, name="django_allauth"),
    path('search/', views.django_search, name="django_search"),
    path('languages/', views.django_languages, name="django_languages"),
]
