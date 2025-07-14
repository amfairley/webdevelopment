from django.shortcuts import render
from django.conf import settings


def backend_home(request):
    '''Return the backend homepage'''
    context = {
    }
    return render(
        request,
        'backend/home/home.html',
        context
    )


def backend_databases(request):
    '''Return the realtional and non-relational databases page'''
    context = {
    }
    return render(
        request,
        'backend/databases/databases.html',
        context
    )


def backend_designing_a_database(request):
    '''Return the designing a database page'''
    context = {
    }
    return render(
        request,
        'backend/designing_a_database/designing_a_database.html',
        context
    )
