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


def backend_sql(request):
    '''Return the SQL page'''
    context = {
    }
    return render(
        request,
        'backend/sql/sql.html',
        context
    )


def backend_postgresql(request):
    '''Return the PostgreSQL page'''
    context = {
    }
    return render(
        request,
        'backend/postgresql/postgresql.html',
        context
    )


def backend_orms(request):
    '''Return the ORMs page'''
    context = {
    }
    return render(
        request,
        'backend/orms/orms.html',
        context
    )
