from django.shortcuts import render


def index(request):

    example_value = 10

    context = {
        'example_value': example_value
    }

    return render(request, 'index.html', context=context)
