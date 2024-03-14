# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializer import ProductSerializer,CategorySerializer
from rest_framework import authentication, permissions
from .models import Product,Category
# # Create your views here.
class Home(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class Categorys(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(["Category"])
@permission_classes([permissions.IsAdminUser,permissions.IsAuthenticated])
def ab (request):
    data = Category.objects.all()
    serializer = CategorySerializer(data,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_products(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def post_products(request):
    return Response()

