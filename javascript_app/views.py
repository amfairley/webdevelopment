from django.shortcuts import render
from django.conf import settings


def JavaScript_home(request):
    '''Return the JavaScript homepage'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/home/home.html',
        context
    )


def JavaScript_variables(request):
    '''Return the JavaScript variable page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/variables/variables.html',
        context
    )
