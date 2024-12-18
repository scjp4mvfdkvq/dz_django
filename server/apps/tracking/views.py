from django.db import transaction
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Operation, Category
from .serializers import OperationSerializer, CategorySerializer
from .serializers import MyTokenObtainPairSerializer

@transaction.atomic
def index(request):
    # Главная страница
    all_operations = Operation.objects.all()
    return render(
        request,
        'tracking/index.html',
        {
            'all_operations': all_operations,
        }
    )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
