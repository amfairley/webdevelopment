from django.shortcuts import render
from django.conf import settings
from .seo import backend_SEO

def backend_home(request):
    '''Return the backend homepage'''
    context = backend_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/home/home.html',
        context
    )


def backend_databases(request):
    '''Return the realtional and non-relational databases page'''
    context = backend_SEO["databases"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/databases/databases.html',
        context
    )


def backend_designing_a_database(request):
    '''Return the designing a database page'''
    context = backend_SEO["designing-a-database"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/designing_a_database/designing_a_database.html',
        context
    )


def backend_sql(request):
    '''Return the SQL page'''
    context = backend_SEO["sql"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/sql/sql.html',
        context
    )


def backend_postgresql(request):
    '''Return the PostgreSQL page'''
    context = backend_SEO["postgresql"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/postgresql/postgresql.html',
        context
    )


def backend_orms(request):
    '''Return the ORMs page'''
    context = backend_SEO["orms"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/orms/orms.html',
        context
    )


def backend_sqlalchemy(request):
    '''Return the SQLAlchemy page'''
    context = backend_SEO["sqlalchemy"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'backend/sqlalchemy/sqlalchemy.html',
        context
    )
