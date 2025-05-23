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


def python_variables(request):
    '''Return the Python variables page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/variables/variables.html',
        context
    )


def python_data_types(request):
    '''Return the Python data types page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/data_types/data_types.html',
        context
    )


def python_strings(request):
    '''Return the Python strings page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/strings/strings.html',
        context
    )
