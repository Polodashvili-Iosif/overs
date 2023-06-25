from django.shortcuts import render


# def index(request):
#     return render(request, 'pages/index.html')


def orders(request):
    return render(request, 'pages/orders.html')


def index(request):
    return render(request, 'pages/tasks.html')


def plan(request):
    return render(request, 'pages/plan.html')


def my_plan(request):
    return render(request, 'pages/my_plan.html')


def map(request):
    return render(request, 'pages/map.html')
