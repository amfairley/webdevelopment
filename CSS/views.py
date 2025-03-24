from django.shortcuts import render
from django.conf import settings


def CSS_home(request):
    '''Return the CSS homepage'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/home/home.html',
        context
    )
