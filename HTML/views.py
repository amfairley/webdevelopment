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
