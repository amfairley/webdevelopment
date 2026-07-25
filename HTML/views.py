from django.shortcuts import render
from django.conf import settings
from .seo import HTML_SEO


def HTML_home(request):
    '''Return the HTML homepage'''
    context = HTML_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])
    return render(
        request,
        'HTML/home/home.html',
        context
    )


def HTML_introducing_elements(request):
    '''Return the HTML introducing elements page'''
    context = HTML_SEO["introducing-elements"].copy()
    context["keywords"] = ", ".join(context["keywords"])
    return render(
        request,
        'HTML/introducing_elements/introducing_elements.html',
        context
    )


def HTML_common_elements(request):
    '''Return the HTML common elements page'''
    context = HTML_SEO["common-elements"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/common_elements/common_elements.html',
        context
    )


def HTML_lists(request):
    '''Return the HTML lists page'''
    context = HTML_SEO["lists"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/lists/lists.html',
        context
    )


def HTML_tables(request):
    '''Return the HTML tables page'''
    context = HTML_SEO["tables"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/tables/tables.html',
        context
    )


def HTML_forms(request):
    '''Return the HTML forms page'''
    context = HTML_SEO["forms"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/forms/forms.html',
        context
    )


def HTML_links(request):
    '''Return the HTML links page'''
    context = HTML_SEO["links"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/links/links.html',
        context
    )


def HTML_media(request):
    '''Return the HTML media page'''
    context = HTML_SEO["media"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/media/media.html',
        context
    )


def HTML_buttons(request):
    '''Return the HTML buttons page'''
    context = HTML_SEO["buttons"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/buttons/buttons.html',
        context
    )


def HTML_semantic(request):
    '''Return the HTML semantics page'''
    context = HTML_SEO["semantic-html"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/semantic/semantic_html.html',
        context
    )


def HTML_accessibility(request):
    '''Return the HTML accessibility page'''
    context = HTML_SEO["html-accessibility-validation"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/accessibility/accessibility.html',
        context
    )


def HTML_example(request):
    '''Return the HTML example page'''
    context = HTML_SEO["html-example"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'HTML/example/example.html',
        context
    )
