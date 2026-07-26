from django.shortcuts import render
from django.conf import settings
from .seo import analytics_SEO

def analytics_home(request):
    '''Return the analytics homepage'''
    context = analytics_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])
    return render(
        request,
        'analytics/home/home.html',
        context
    )


def analytics_seo(request):
    '''Return the analytics seo page'''
    context = analytics_SEO["seo"].copy()
    context["keywords"] = ", ".join(context["keywords"])
    return render(
        request,
        'analytics/seo/seo.html',
        context
    )
