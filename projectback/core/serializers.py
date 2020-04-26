from rest_framework import serializers
from core.models import *


class CategoriesListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category()
        category.name = validated_data.get('name', 'default name')
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.id')

    class Meta:
        model = Products
        fields = "__all__"


class BasketSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Basket
        fields = {'id', 'products'}