# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from best_price.models import Product
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.core import serializers


def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# def get_products(request):
#     product_list = list(Product.objects.all().values_list("title", flat=True))
#     print(product_list)
#     return JsonResponse(dict(title=product_list))


# def hello_world(request):
#     return render(request, 'hello_world.html', {
#         'current_time': str(datetime.now()),
#     })


def get_product(request, name):
    # try:
    # p = Product.objects.get(title=name)
    return HttpResponse(serializers.serialize("json", Product.objects.filter(title=name)))
    # except DoesNotExist:
    #     print("Either the entry or blog doesn't exist.")


def get_products(request, page_num, page_size=10):
    products = list(Product.objects.values())
    page = int(page_num)
    size = int(page_size)
    total_size = Product.objects.count()
    # if total_size <= page * size - size:
    #     return HttpResponseNotFound('<h1>It is already the end of list</h1>')
    # elif total_size < page * size:
    #     return HttpResponse(serializers.serialize("json", products[page * size - size:]))
    # else:
    #     return HttpResponse(serializers.serialize("json", products[page * size - size:page * size]))

    print(products)
    if total_size <= page * size - size:
        return HttpResponseNotFound('<h1>It is already the end of list</h1>')
    elif total_size < page * size:
        return JsonResponse(products[page * size - size:], safe=False)
    else:
        return JsonResponse(products[page * size - size:page * size], safe=False)


def create_product(request, title, price, cat, loc):
    # title = request.GET.get("title", "")
    # price = request.GET.get("price", "")
    Product.objects.create(title=title, price=float(price), category=cat, location=loc)
    return HttpResponse('Success')


def update_product(request, id, title, price, cat, loc):
    try:
        product = Product.objects.get(pk=id)
        print("product:", product)
        product.title = title
        product.price = float(price)
        product.category = cat
        product.location = loc
        product.save()
        # Cannot do update() using get() because the return type is an object
        # Pycharm show the return type of get() is Queryset?
        # result = product.update(title=title, price=float(price), category=cat, location=loc)
        return HttpResponse('Success')
    except:
        return HttpResponse('Nothing changed')


def search_product(request, keyword):
    result = Product.objects.filter(title__contains=keyword)
    if result.exists():
        return HttpResponse(serializers.serialize("json", result))
    else:
        return HttpResponse('There is not such product')
"""
Get_product_list
Get the list of product in page_number, the default page_size=10
Input: page_number
Return: product list including id, title, price in page_number

Get_product
Get a specific product detail
Input: product id
Return: product id, title, price, category, buy_location

New_product
Create a new product with title and price
Input: product title, price
Return: ok

Update_product
Update existing product
Input: product id, other product info like title, price, category, and buy_location
Return: ok

Seach_product
Search product with keyword
Input: keyword
Return: keyword related product list with title and price
"""
