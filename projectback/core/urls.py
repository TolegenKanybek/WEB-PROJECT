from django.contrib import admin
from django.urls import path
from core.views.views_fbv import *
from core.views.views_cbv import *
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('categories', CategoriesListAPIView.as_view()),
    path('clothes', products),
    path('categories/<int:id>/clothes', products_in_category),
    path('clothes/<int:id>', ProductDetails.as_view()),
    path('card/clothes', products_in_basket),
    path('card/clothes/<int:id>', BasketProduct.as_view()),
    # path('clothes', ClothesListAPIView.as_view()),
    path('clothes/<int:id>', productsOfCategory),
    path('categories/<int:id>', category),
    #path('clothes/new', newClothesList.as_view()),
]
