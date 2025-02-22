from django.shortcuts import render
from django.conf import settings


def intro_to_full_stack(request):
    '''Return the introduction to full stack page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'intro_to_full_stack/introduction_to_full_stack.html',
        context
    )
