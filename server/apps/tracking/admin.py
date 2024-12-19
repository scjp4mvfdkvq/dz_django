from django.contrib import admin
from .models import Operation, Category


# admin.site.register(Operation)

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'operation_at') # поля для отображения в списке объектов
    list_filter = ('operation_at',) # фильтр по дате создания
    search_fields = ('name',) # поиск по имени
    ordering = ('-operation_at',) # сортировка по дате создания

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # поля для отображения в списке объектов
