from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    return HttpResponse('Домашняя страница')


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    res = DATA['omlet']
    res_1 = dict(res)
    for key in res_1:
        res_1[key] = res_1[key] * servings
    context = {'item': res_1,
               'servings': servings, }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    res = DATA['pasta']
    res_1 = dict(res)
    for key in res_1:
        res_1[key] = res_1[key] * servings
    context = {'item': res_1,
               'servings': servings, }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    res = DATA['buter']
    res_1 = dict(res)
    for key in res_1:
        res_1[key] = res_1[key] * servings
    context = {'item': res_1,
               'servings': servings, }
    return render(request, 'calculator/index.html', context)

