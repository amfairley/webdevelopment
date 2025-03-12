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
