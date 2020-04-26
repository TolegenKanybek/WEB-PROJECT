from core.models import *
from core.serializers import *
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ClothesListAPIView(APIView):
    def get(self, request):
        product_list = Products.objects.all()
        serializer = ProductListSerializer(product_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductListSerializer


class CategoriesListAPIView(APIView):
    def get(self, request):
        categories_list = Category.objects.all()
        serializer = CategoriesListSerializer(categories_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BasketProduct(APIView):
    def get_object(self, id):
        try:
            return Products.objects.get(id=id)
        except Products.DoesNotExist as e:
            return Response({'error': str(e)})

    def delete(self, request, pk):
        product = self.get_object(pk)
        basket = Basket.objects.get(id=2)
        basket.products.remove(product)
        return Response({'DELETED': True})


class newProductList(APIView):
    def get(self, request):
        product_list = Products.objects.get_new_products()
        serializer = ProductListSerializer(product_list, many=True)
        return Response(serializer.data)
