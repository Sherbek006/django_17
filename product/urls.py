from django.urls import path, include
from .views import Home,Categorys,get_products,ab
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'products',Home, basename='products')
router.register(r'category',Categorys,basename='category')

urlpatterns = [
    path('',include(router.urls)),
    path('products',get_products),
    path('Category',ab)
]

