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


def sector_map(request):
    return render(request, 'pages/sector_map.html')


def fertilizers(request):
    return render(request, 'pages/fertilizers.html')


def route(request, name):
    return render(request, 'pages/route.html', {'name': name})
