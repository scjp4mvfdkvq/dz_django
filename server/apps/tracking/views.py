from datetime import datetime

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Operation, Category
from .utils import convert_price_to_eur
from .serializers import OperationSerializer, CategorySerializer



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