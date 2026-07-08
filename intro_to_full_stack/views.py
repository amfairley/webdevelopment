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


def full_stack_website_development(request):
    '''Return the introduction to full stack web development page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/website_development/website_development.html',
        context
    )


def full_stack_sizes(request):
    '''Return the introduction to full stack sizes page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/sizes/sizes.html',
        context
    )


def full_stack_colour(request):
    '''Return the introduction to full stack colour page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/colour/colour.html',
        context
    )


def full_stack_project_goals(request):
    '''Return the introduction to full stack project goals page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/project_goals/project_goals.html',
        context
    )


def full_stack_user_stories(request):
    '''Return the introduction to full stack user stories page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/user_stories/user_stories.html',
        context
    )


def full_stack_five_stages(request):
    '''Return the introduction to full stack five stages of UI/UX page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/five_stages/five_stages.html',
        context
    )


def full_stack_features(request):
    '''Return the introduction to full stack features page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/features/features.html',
        context
    )


def full_stack_testing(request):
    '''Return the introduction to full stack testing page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/testing/testing.html',
        context
    )


def full_stack_google_dev_tools(request):
    '''Return the introduction to full stack Google DevTools page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/google_dev_tools/google_dev_tools.html',
        context
    )


def full_stack_readme(request):
    '''Return the introduction to full stack README.md page'''
    context = {
    }
    return render(
        request,
        'intro_to_full_stack/readme/readme.html',
        context
    )
