from django.shortcuts import render
from django.conf import settings


def python_home(request):
    '''Return the Python homepage'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/home/home.html',
        context
    )
