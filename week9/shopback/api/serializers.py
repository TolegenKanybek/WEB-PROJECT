from rest_framework import serializers
from .model import Product, Category

class ProductSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model=Product
        fields=('name','price','description','price')


class CategorySerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model=Category
        fields=('name')

