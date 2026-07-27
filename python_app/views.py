from django.shortcuts import render
from django.conf import settings
from .seo import python_SEO

def python_home(request):
    '''Return the Python homepage'''
    context = python_SEO["home"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/home/home.html',
        context
    )


def python_variables(request):
    '''Return the Python variables page'''
    context = python_SEO["variables"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/variables/variables.html',
        context
    )


def python_data_types(request):
    '''Return the Python data types page'''
    context = python_SEO["data-types"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/data_types/data_types.html',
        context
    )


def python_strings(request):
    '''Return the Python strings page'''
    context = python_SEO["strings"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/strings/strings.html',
        context
    )


def python_booleans(request):
    '''Return the Python booleans page'''
    context = python_SEO["booleans"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/booleans/booleans.html',
        context
    )


def python_lists(request):
    '''Return the Python lists page'''
    context = python_SEO["lists"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/lists/lists.html',
        context
    )


def python_tuples(request):
    '''Return the Python tuples page'''
    context = python_SEO["tuples"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/tuples/tuples.html',
        context
    )


def python_dictionaries(request):
    '''Return the Python dictionaries page'''
    context = python_SEO["dictionaries"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/dictionaries/dictionaries.html',
        context
    )


def python_sets(request):
    '''Return the Python sets page'''
    context = python_SEO["sets"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/sets/sets.html',
        context
    )


def python_regular_expressions(request):
    '''Return the Python regular expressions page'''
    context = python_SEO["regular-expressions"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/regular_expressions/regular_expressions.html',
        context
    )


def python_functions(request):
    '''Return the Python functions page'''
    context = python_SEO["functions"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/functions/functions.html',
        context
    )


def python_input(request):
    '''Return the Python input page'''
    context = python_SEO["input"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/input/input.html',
        context
    )


def python_os(request):
    '''Return the Python OS page'''
    context = python_SEO["os"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/os/os.html',
        context
    )


def python_math(request):
    '''Return the Python math page'''
    context = python_SEO["math"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/math/math.html',
        context
    )


def python_datetime(request):
    '''Return the Python datetime page'''
    context = python_SEO["datetime"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/datetime/datetime.html',
        context
    )


def python_pandas(request):
    '''Return the Python pandas page'''
    context = python_SEO["pandas"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/pandas/pandas.html',
        context
    )


def python_numpy(request):
    '''Return the Python numpy page'''
    context = python_SEO["numpy"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/numpy/numpy.html',
        context
    )


def python_csv(request):
    '''Return the Python csv page'''
    context = python_SEO["csv"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/csv/csv.html',
        context
    )


def python_json(request):
    '''Return the Python json page'''
    context = python_SEO["json"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/json/json.html',
        context
    )


def python_pillow(request):
    '''Return the Python pillow page'''
    context = python_SEO["pillow"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/pillow/pillow.html',
        context
    )


def python_scope(request):
    '''Return the Python scope page'''
    context = python_SEO["scope"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/scope/scope.html',
        context
    )


def python_loops(request):
    '''Return the Python loops page'''
    context = python_SEO["loops"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/loops/loops.html',
        context
    )


def python_conditionals(request):
    '''Return the Python conditionals page'''
    context = python_SEO["conditionals"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/conditionals/conditionals.html',
        context
    )


def python_classes(request):
    '''Return the Python classes page'''
    context = python_SEO["classes"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/classes/classes.html',
        context
    )


def python_unit_testing(request):
    '''Return the Python unit testing page'''
    context = python_SEO["unit-testing"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/unit_testing/unit_testing.html',
        context
    )


def python_data_and_api_requests(request):
    '''Return the Python data and API requests page'''
    context = python_SEO["data-and-api-requests"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/data_and_api_requests/data_and_api_requests.html',
        context
    )


def python_code_validation(request):
    '''Return the Python code validation page'''
    context = python_SEO["code-validation"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/code_validation/code_validation.html',
        context
    )


def python_google_sheets_program(request):
    '''Return the Python google sheets program page'''
    context = python_SEO["google-sheets-program"].copy()
    context["keywords"] = ", ".join(context["keywords"])

    return render(
        request,
        'python_app/google_sheets_program/google_sheets_program.html',
        context
    )
