from django.shortcuts import render
from django.conf import settings


def deployment_home(request):
    '''Return the deployment homepage'''
    context = {
    }
    return render(
        request,
        'deployment/home/home.html',
        context
    )
