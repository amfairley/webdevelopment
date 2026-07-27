from django.shortcuts import render
from django.conf import settings
from .seo import django_SEO


def django_home(request):
    '''Return the Django homepage'''
    context = django_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/home/home.html',
        context
    )


def django_getting_started_with_django(request):
    '''Return the getting started with Django page'''
    context = django_SEO["getting-started-with-django"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/getting_started_with_django/getting_started_with_django.html',
        context
    )


def django_admin(request):
    '''Return the admin page'''
    context = django_SEO["admin"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/admin/admin.html',
        context
    )


def django_settings(request):
    '''Return the settings page'''
    context = django_SEO["settings"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/settings/settings.html',
        context
    )


def django_urls(request):
    '''Return the urls page'''
    context = django_SEO["urls"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/urls/urls.html',
        context
    )


def django_apps(request):
    '''Return the apps page'''
    context = django_SEO["apps"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/apps/apps.html',
        context
    )


def django_templates(request):
    '''Return the templates page'''
    context = django_SEO["templates"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/templates/templates.html',
        context
    )


def django_views(request):
    '''Return the views page'''
    context = django_SEO["views"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/views/views.html',
        context
    )


def django_models(request):
    '''Return the models page'''
    context = django_SEO["models"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/models/models.html',
        context
    )


def django_forms(request):
    '''Return the forms page'''
    context = django_SEO["forms"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/forms/forms.html',
        context
    )


def django_templating_language(request):
    '''Return the templating language page'''
    context = django_SEO["templating-language"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/templating_language/templating_language.html',
        context
    )


def django_error_pages(request):
    '''Return the error pages page'''
    context = django_SEO["error-pages"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/error_pages/error_pages.html',
        context
    )


def django_crud(request):
    '''Return the crud page'''
    context = django_SEO["crud"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/crud/crud.html',
        context
    )


def django_messages(request):
    '''Return the messages page'''
    context = django_SEO["messages"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/messages/messages.html',
        context
    )


def django_static(request):
    '''Return the static page'''
    context = django_SEO["static"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/static/static.html',
        context
    )


def django_testing(request):
    '''Return the testing page'''
    context = django_SEO["testing"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/testing/testing.html',
        context
    )


def django_allauth(request):
    '''Return the allauth page'''
    context = django_SEO["allauth"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/allauth/allauth.html',
        context
    )


def django_search(request):
    '''Return the search page'''
    context = django_SEO["search"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/search/search.html',
        context
    )


def django_languages(request):
    '''Return the languages page'''
    context = django_SEO["languages"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/languages/languages.html',
        context
    )


def django_envpy(request):
    '''Return the env.py page'''
    context = django_SEO["envpy"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'django_app/envpy/envpy.html',
        context
    )
