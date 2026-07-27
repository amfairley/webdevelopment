from django.shortcuts import render
from django.conf import settings
from .seo import javascript_SEO

def JavaScript_home(request):
    '''Return the JavaScript homepage'''
    context = javascript_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/home/home.html',
        context
    )


def JavaScript_variables(request):
    '''Return the JavaScript variable page'''
    context = javascript_SEO["variables"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/variables/variables.html',
        context
    )


def JavaScript_scope(request):
    '''Return the JavaScript scope page'''
    context = javascript_SEO["scope"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/scope/scope.html',
        context
    )


def JavaScript_data_types(request):
    '''Return the JavaScript data types page'''
    context = javascript_SEO["data-types"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/data_types/data_types.html',
        context
    )


def JavaScript_math(request):
    '''Return the JavaScript math page'''
    context = javascript_SEO["math"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/math/math.html',
        context
    )


def JavaScript_arrays(request):
    '''Return the JavaScript arrays page'''
    context = javascript_SEO["arrays"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/arrays/arrays.html',
        context
    )


def JavaScript_sets(request):
    '''Return the JavaScript sets page'''
    context = javascript_SEO["sets"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/sets/sets.html',
        context
    )


def JavaScript_objects(request):
    '''Return the JavaScript objects page'''
    context = javascript_SEO["objects"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/objects/objects.html',
        context
    )


def JavaScript_console_commands(request):
    '''Return the JavaScript console commands page'''
    context = javascript_SEO["console-commands"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/console_commands/console_commands.html',
        context
    )


def JavaScript_functions(request):
    '''Return the JavaScript functions page'''
    context = javascript_SEO["functions"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/functions/functions.html',
        context
    )


def JavaScript_conditional_statements(request):
    '''Return the JavaScript conditional statements page'''
    context = javascript_SEO["conditional-statements"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/conditional_statements/conditional_statements.html',
        context
    )


def JavaScript_for_loops(request):
    '''Return the JavaScript for loops page'''
    context = javascript_SEO["for-loops"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/for_loops/for_loops.html',
        context
    )


def JavaScript_while_loops(request):
    '''Return the JavaScript while loops page'''
    context = javascript_SEO["while-loops"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/while_loops/while_loops.html',
        context
    )


def JavaScript_try(request):
    '''Return the JavaScript try page'''
    context = javascript_SEO["try"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/try/try.html',
        context
    )


def JavaScript_nested_loops(request):
    '''Return the JavaScript nested loops page'''
    context = javascript_SEO["nested-loops"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/nested_loops/nested_loops.html',
        context
    )


def JavaScript_the_dom(request):
    '''Return the JavaScript dom page'''
    context = javascript_SEO["the-dom"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/the_dom/the_dom.html',
        context
    )


def JavaScript_targeting_the_dom(request):
    '''Return the JavaScript targeting the dom page'''
    context = javascript_SEO["targeting-the-dom"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/targeting_the_dom/targeting_the_dom.html',
        context
    )


def JavaScript_manipulating_the_dom(request):
    '''Return the JavaScript manipulating the dom page'''
    context = javascript_SEO["manipulating-the-dom"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/manipulating_the_dom/manipulating_the_dom.html',
        context
    )


def JavaScript_events(request):
    '''Return the JavaScript events page'''
    context = javascript_SEO["events"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/events/events.html',
        context
    )


def JavaScript_jquery(request):
    '''Return the JavaScript jquery page'''
    context = javascript_SEO["jquery"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/jquery/jquery.html',
        context
    )


def JavaScript_debugging(request):
    '''Return the JavaScript debugging page'''
    context = javascript_SEO["debugging"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/debugging/debugging.html',
        context
    )


def JavaScript_validation(request):
    '''Return the JavaScript validation page'''
    context = javascript_SEO["validation"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/validation/validation.html',
        context
    )


def JavaScript_emailjs(request):
    '''Return the JavaScript EmailJs page'''
    context = javascript_SEO["emailjs"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'javascript_app/emailjs/emailjs.html',
        context
    )
