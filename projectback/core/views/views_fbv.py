from core.models import *
from core.serializers import *
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'PUT', 'DELETE'])
def category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = CategoriesListSerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriesListSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    if request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        clothes_list = Products.objects.all()
        serializer = ProductListSerializer(clothes_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def products_in_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        products = category.product_set.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def products_in_basket(request):
    try:
        basket = Basket.objects.get(id=2)
    except Basket.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        products = basket.products.all()
        serializer = ProductListSerializer(clothes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductListSerializer(data=request.data)


@api_view(['GET'])
def productsOfCategory(request, id):
    if request.method == 'GET':
        product_list = Products.objects.all()
        productsOfCategory = []
        for product in product_list:
            if product.category.id == id:
                serializer = ProductListSerializer(product)
                productsOfCategory.append(serializer.data)
        return Response(productsOfCategory)
