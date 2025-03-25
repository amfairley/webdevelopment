from django.shortcuts import render
from django.conf import settings


def CSS_home(request):
    '''Return the CSS homepage'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/home/home.html',
        context
    )


def CSS_selectors(request):
    '''Return the CSS selectors page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/selectors/selectors.html',
        context
    )


def CSS_box_model(request):
    '''Return the CSS box model page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/box_model/the_css_box_model.html',
        context
    )


def CSS_display_and_positioning(request):
    '''Return the CSS display and positioning page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/display_and_positioning/display_and_positioning.html',
        context
    )
