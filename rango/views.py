from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from rango.models import Category, Page

def index(request):
    categoryList = Category.objects.order_by('-likes')[:5]
    contextDict = {'categories': categoryList}
    return render(request, 'rango/index.html', contextDict)

def about(request):
    context_dict = {'message': "This is rango's cousin. can't you see the resemblance ?"}
    return render(request, 'rango/about.html', context_dict)

def category(request, categoryNameSlug):
    try:
        category = Category.objects.get(slug=categoryNameSlug)
        contextDict = {'categoryName': category.name}
        pages = Page.objects.filter(category = category)
        contextDict['category'] = category
        contextDict['pages'] = pages

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/categories.html', contextDict)

