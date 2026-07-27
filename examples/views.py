from django.shortcuts import render
from django.conf import settings
from .seo import examples_SEO

def examples(request):
    '''Return the examples'''
    context = examples_SEO["examples"].copy()
    context["keywords"] = ", ".join(context["keywords"])
    return render(
        request,
        'examples/examples/examples.html',
        context
    )
