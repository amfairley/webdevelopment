from django.shortcuts import render
from django.conf import settings


def full_stack_programming_and_the_web(request):
    '''Return the introduction to full stack progamming and the web page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/programming_and_the_web/programming_and_the_web.html',
        context
    )


def full_stack_github(request):
    '''Return the introduction to full stack github page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/github/github.html',
        context
    )