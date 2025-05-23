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


def python_booleans(request):
    '''Return the Python booleans page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/booleans/booleans.html',
        context
    )


def python_lists(request):
    '''Return the Python lists page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/lists/lists.html',
        context
    )


def python_tuples(request):
    '''Return the Python tuples page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/tuples/tuples.html',
        context
    )


def python_dictionaries(request):
    '''Return the Python dictionaries page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/dictionaries/dictionaries.html',
        context
    )


def python_sets(request):
    '''Return the Python sets page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/sets/sets.html',
        context
    )


def python_regular_expressions(request):
    '''Return the Python regular expressions page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'python_app/regular_expressions/regular_expressions.html',
        context
    )
