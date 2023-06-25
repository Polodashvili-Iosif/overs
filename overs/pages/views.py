from django.shortcuts import render, get_object_or_404

from . import models

# def index(request):
#     return render(request, 'pages/index.html')


def orders(request):
    return render(request, 'pages/orders.html')


def index(request, id, optional_arg=None):
    task = get_object_or_404(models.Task, id=id)
    return render(request, 'pages/tasks.html', {'task': task})


def plan(request):
    return render(request, 'pages/plan.html')


def my_plan(request):
    plans = models.Plan.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'pages/my_plan_2.html', context)


def map(request):
    return render(request, 'pages/map.html')


def sector_map(request):
    return render(request, 'pages/sector_map.html')


def fertilizers(request):
    elements = models.Element.objects.all()
    context = {
        'elements': elements
    }
    return render(request, 'pages/fertilizers.html', context)


def route(request, name):
    return render(request, 'pages/route.html', {'name': name})
