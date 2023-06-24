from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def orders(request):
    return render(request, 'pages/orders.html')


def tasks(request):
    return render(request, 'pages/tasks.html')


def plan(request):
    return render(request, 'pages/plan.html')
