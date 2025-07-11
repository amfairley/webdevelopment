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


def flask_database(request):
    '''Return the Flask creating the database page'''
    context = {
    }
    return render(
        request,
        'flask_app/database/database.html',
        context
    )


def flask_template(request):
    '''Return the Flask template inheritance page'''
    context = {
    }
    return render(
        request,
        'flask_app/template/template.html',
        context
    )


def flask_create(request):
    '''Return the Flask create records page'''
    context = {
    }
    return render(
        request,
        'flask_app/create/create.html',
        context
    )


def flask_read(request):
    '''Return the Flask read records page'''
    context = {
    }
    return render(
        request,
        'flask_app/read/read.html',
        context
    )
