from django.shortcuts import render
from django.conf import settings
from .seo import flask_SEO

def flask_home(request):
    '''Return the Flask homepage'''
    context = flask_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/home/home.html',
        context
    )


def flask_basics(request):
    '''Return the Flask setting up the basics page'''
    context = flask_SEO["basics"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/basics/basics.html',
        context
    )


def flask_database(request):
    '''Return the Flask creating the database page'''
    context = flask_SEO["database"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/database/database.html',
        context
    )


def flask_template(request):
    '''Return the Flask template inheritance page'''
    context = flask_SEO["template"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/template/template.html',
        context
    )


def flask_create(request):
    '''Return the Flask create records page'''
    context = flask_SEO["create"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/create/create.html',
        context
    )


def flask_read(request):
    '''Return the Flask read records page'''
    context = flask_SEO["read"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/read/read.html',
        context
    )


def flask_update(request):
    '''Return the Flask update records page'''
    context = flask_SEO["update"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/update/update.html',
        context
    )


def flask_delete(request):
    '''Return the Flask delete records page'''
    context = flask_SEO["delete"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'flask_app/delete/delete.html',
        context
    )
