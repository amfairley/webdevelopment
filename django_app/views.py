from django.shortcuts import render
from django.conf import settings


def django_home(request):
    '''Return the Django homepage'''
    context = {
    }
    return render(
        request,
        'django_app/home/home.html',
        context
    )


def django_getting_started_with_django(request):
    '''Return the getting started with Django page'''
    context = {
    }
    return render(
        request,
        'django_app/getting_started_with_django/getting_started_with_django.html',
        context
    )


def django_admin(request):
    '''Return the admin page'''
    context = {
    }
    return render(
        request,
        'django_app/admin/admin.html',
        context
    )


def django_settings(request):
    '''Return the settings page'''
    context = {
    }
    return render(
        request,
        'django_app/settings/settings.html',
        context
    )


def django_urls(request):
    '''Return the urls page'''
    context = {
    }
    return render(
        request,
        'django_app/urls/urls.html',
        context
    )


def django_apps(request):
    '''Return the apps page'''
    context = {
    }
    return render(
        request,
        'django_app/apps/apps.html',
        context
    )


def django_templates(request):
    '''Return the templates page'''
    context = {
    }
    return render(
        request,
        'django_app/templates/templates.html',
        context
    )


def django_views(request):
    '''Return the views page'''
    context = {
    }
    return render(
        request,
        'django_app/views/views.html',
        context
    )


def django_models(request):
    '''Return the models page'''
    context = {
    }
    return render(
        request,
        'django_app/models/models.html',
        context
    )


def django_forms(request):
    '''Return the forms page'''
    context = {
    }
    return render(
        request,
        'django_app/forms/forms.html',
        context
    )


def django_templating_language(request):
    '''Return the templating language page'''
    context = {
    }
    return render(
        request,
        'django_app/templating_language/templating_language.html',
        context
    )


def django_error_pages(request):
    '''Return the error pages page'''
    context = {
    }
    return render(
        request,
        'django_app/error_pages/error_pages.html',
        context
    )


def django_crud(request):
    '''Return the crud page'''
    context = {
    }
    return render(
        request,
        'django_app/crud/crud.html',
        context
    )


def django_messages(request):
    '''Return the messages page'''
    context = {
    }
    return render(
        request,
        'django_app/messages/messages.html',
        context
    )


def django_static(request):
    '''Return the static page'''
    context = {
    }
    return render(
        request,
        'django_app/static/static.html',
        context
    )


def django_testing(request):
    '''Return the testing page'''
    context = {
    }
    return render(
        request,
        'django_app/testing/testing.html',
        context
    )


def django_allauth(request):
    '''Return the allauth page'''
    context = {
    }
    return render(
        request,
        'django_app/allauth/allauth.html',
        context
    )


def django_search(request):
    '''Return the search page'''
    context = {
    }
    return render(
        request,
        'django_app/search/search.html',
        context
    )


def django_languages(request):
    '''Return the languages page'''
    context = {
    }
    return render(
        request,
        'django_app/languages/languages.html',
        context
    )
