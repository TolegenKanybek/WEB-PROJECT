from django.urls import include, path
from rest_framework import routers
#from . import views
from django.views import product_list, category_list, product_category, product_detail, category_detail 

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('category/', category_list),
    path('category/<int:category_id>/', category_detail),
    path('category/<int:category_id>/products/', product_category),
]