from django.shortcuts import render
from django.conf import settings


def flask_home(request):
    '''Return the Flask homepage'''
    context = {
    }
    return render(
        request,
        'flask_app/home/home.html',
        context
    )


def flask_basics(request):
    '''Return the Flask setting up the basics page'''
    context = {
    }
    return render(
        request,
        'flask_app/basics/basics.html',
        context
    )
