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


def CSS_flexbox(request):
    '''Return the CSS flexbox page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/flexbox/flexbox.html',
        context
    )


def CSS_grids(request):
    '''Return the CSS grids page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/grids/grids.html',
        context
    )


def CSS_backgrounds(request):
    '''Return the CSS backgrounds page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/backgrounds/backgrounds.html',
        context
    )


def CSS_visibility_and_z_positioning(request):
    '''Return the CSS visibility and z positioning page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/visibility_and_z_positioning/visibility_and_z_positioning.html',
        context
    )


def CSS_cursor(request):
    '''Return the CSS cursor page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/cursor/cursor.html',
        context
    )


def CSS_typography(request):
    '''Return the CSS typography page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/typography/typography.html',
        context
    )


def CSS_links_and_buttons(request):
    '''Return the CSS links_and_buttons page'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'CSS/links_and_buttons/links_and_buttons.html',
        context
    )
