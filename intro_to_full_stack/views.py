from django.shortcuts import render
from django.conf import settings


def full_stack_programming_and_the_web(request):
    '''Return the introduction to full stack page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'intro_to_full_stack/programming_and_the_web/programming_and_the_web.html',
        context
    )
