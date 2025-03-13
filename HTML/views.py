from django.shortcuts import render
from django.conf import settings


def HTML_home(request):
    '''Return the HTML homepage'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/home/home.html',
        context
    )


def HTML_introducing_elements(request):
    '''Return the HTML introducing elements page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/introducing_elements/introducing_elements.html',
        context
    )


def HTML_common_elements(request):
    '''Return the HTML common elements page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/common_elements/common_elements.html',
        context
    )


def HTML_lists(request):
    '''Return the HTML lists page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/lists/lists.html',
        context
    )


def HTML_tables(request):
    '''Return the HTML tables page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/tables/tables.html',
        context
    )


def HTML_forms(request):
    '''Return the HTML forms page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/forms/forms.html',
        context
    )


def HTML_links(request):
    '''Return the HTML links page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/links/links.html',
        context
    )


def HTML_media(request):
    '''Return the HTML media page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/media/media.html',
        context
    )


def HTML_buttons(request):
    '''Return the HTML buttons page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'HTML/buttons/buttons.html',
        context
    )
