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


def JavaScript_scope(request):
    '''Return the JavaScript scope page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/scope/scope.html',
        context
    )


def JavaScript_data_types(request):
    '''Return the JavaScript data types page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/data_types/data_types.html',
        context
    )


def JavaScript_math(request):
    '''Return the JavaScript math page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/math/math.html',
        context
    )


def JavaScript_arrays(request):
    '''Return the JavaScript arrays page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/arrays/arrays.html',
        context
    )


def JavaScript_sets(request):
    '''Return the JavaScript sets page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/sets/sets.html',
        context
    )


def JavaScript_objects(request):
    '''Return the JavaScript objects page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'javascript_app/objects/objects.html',
        context
    )
