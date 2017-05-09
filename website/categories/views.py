from django.http import HttpResponse
from .models import Category
from django.http import Http404
from django.shortcuts import render


def index(request):
    all_categories = Category.objects.all()
    context = {'all_categories': all_categories}
    return render(request, 'categories/index.html', context)


def category(request, cat_id):
    try:
        category = Category.objects.get(id=cat_id)
    except Category.DoesNotExist:
        raise Http404("Category Does Not Exist")
    return render(request, 'categories/category.html', {'category': category})