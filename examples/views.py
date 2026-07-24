from django.shortcuts import render
from django.conf import settings


def examples(request):
    '''Return the examples'''
    context = {
    }
    return render(
        request,
        'examples/examples/examples.html',
        context
    )
