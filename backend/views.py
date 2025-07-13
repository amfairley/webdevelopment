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
    '''Return the realtional and non-relational databases homepage'''
    context = {
    }
    return render(
        request,
        'backend/databases/databases.html',
        context
    )
