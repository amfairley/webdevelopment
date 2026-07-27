from django.shortcuts import render
from django.conf import settings
from .seo import deployment_SEO

def deployment_home(request):
    '''Return the deployment homepage'''
    context = deployment_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'deployment/home/home.html',
        context
    )
