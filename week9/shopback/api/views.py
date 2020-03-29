from django.shortcuts import render
from rest_framework import viewsets
from django.http.response import JsonResponse
from django.http import Http404 

from api.models import Product,Category



#class ProductViewSet(viewsets.ModelViewSet):
   # queryset=Product.objects.all().order_by('name')
    #serializer_class=ProductSerializer


#class CategoryViewSet(viewsets.ModelViewSet):
    #queryset=Category.objects.all().order_by('name')
    #serializer_class=CategorySerializer

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'product does not exists'})

    return JsonResponse(product.to_json())


def category_list(request):
    categorys = Category.objects.all()
    category_json = [category.to_json() for category in categorys]
    return JsonResponse(category_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not exists'})
    return JsonResponse(category.to_json())


def product_category(request, category_id):
    try:
        products = Product.objects.filter(category_id=category_id)
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)})
