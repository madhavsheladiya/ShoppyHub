from math import ceil
from unicodedata import category

from django.shortcuts import render

# Create your views here.
from shop.models import Category, Product


def search_match(query, item):
    '''return true only if query matches the item'''
    if query.upper() in item.description.upper() or query.upper() in item.name.upper():
        return True
    else:
        return False


def search(request):
    global products
    query = request.GET.get('search')
    products = []
   # categories = Category.objects.all()
    prods = Product.objects.all()
    #cat_prods = Product.objects.values('category', 'id')
    #cats = {item['category'] for item in cat_prods}
    #for cat in cats:
        #products_temp = Product.objects.filter(category=cat)

    for item_tmp in prods:
            if search_match(query, item_tmp):
                products.append(item_tmp)

    context = {
        #'category': category,
        #'categories': categories,

        'products': products
    }
    return render(request, 'shop/product/list.html', context)
