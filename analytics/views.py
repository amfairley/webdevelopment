from django.shortcuts import render
from django.conf import settings


def analytics_home(request):
    '''Return the analytics homepage'''
    context = {
    }
    return render(
        request,
        'analytics/home/home.html',
        context
    )