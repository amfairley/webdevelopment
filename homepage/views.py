from django.shortcuts import render
from django.conf import settings
from .seo import home_SEO

def index(request):
    '''Return the homepage'''
    context = home_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'homepage/index.html',
        context
    )


def example(request):
    '''Return an example homepage'''
    context = {
    }
    return render(
        request,
        'homepage/example/example.html',
        context
    )
