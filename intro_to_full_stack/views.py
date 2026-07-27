from django.shortcuts import render
from django.conf import settings
from .seo import intro_SEO

def full_stack_programming_and_the_web(request):
    '''Return the introduction to full stack progamming and the web page'''
    context = intro_SEO["programming-and-the-web"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/programming_and_the_web/programming_and_the_web.html',
        context
    )


def full_stack_github(request):
    '''Return the introduction to full stack github page'''
    context = intro_SEO["github"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/github/github.html',
        context
    )


def full_stack_website_development(request):
    '''Return the introduction to full stack web development page'''
    context = intro_SEO["website-development"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/website_development/website_development.html',
        context
    )


def full_stack_sizes(request):
    '''Return the introduction to full stack sizes page'''
    context = intro_SEO["sizes"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/sizes/sizes.html',
        context
    )


def full_stack_colour(request):
    '''Return the introduction to full stack colour page'''
    context = intro_SEO["colour"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/colour/colour.html',
        context
    )


def full_stack_project_goals(request):
    '''Return the introduction to full stack project goals page'''
    context = intro_SEO["project-goals"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/project_goals/project_goals.html',
        context
    )


def full_stack_user_stories(request):
    '''Return the introduction to full stack user stories page'''
    context = intro_SEO["user-stories"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/user_stories/user_stories.html',
        context
    )


def full_stack_five_stages(request):
    '''Return the introduction to full stack five stages of UI/UX page'''
    context = intro_SEO["five-stages"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/five_stages/five_stages.html',
        context
    )


def full_stack_features(request):
    '''Return the introduction to full stack features page'''
    context = intro_SEO["features"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/features/features.html',
        context
    )


def full_stack_testing(request):
    '''Return the introduction to full stack testing page'''
    context = intro_SEO["testing"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/testing/testing.html',
        context
    )


def full_stack_google_dev_tools(request):
    '''Return the introduction to full stack Google DevTools page'''
    context = intro_SEO["google-dev-tools"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/google_dev_tools/google_dev_tools.html',
        context
    )


def full_stack_readme(request):
    '''Return the introduction to full stack README.md page'''
    context = intro_SEO["readme"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/readme/readme.html',
        context
    )


def full_stack_vscode(request):
    '''Return the introduction to full stack VS Code page'''
    context = intro_SEO["vscode"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/vscode/vscode.html',
        context
    )


def full_stack_pseudocode(request):
    '''Return the introduction to full stack Pseudocode'''
    context = intro_SEO["pseudocode"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'intro_to_full_stack/pseudocode/pseudocode.html',
        context
    )
