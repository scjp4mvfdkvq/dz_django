from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.db import transaction

from .models import Operation
from .utils import convert_price_to_eur



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

