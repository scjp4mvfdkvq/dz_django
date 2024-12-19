from django.contrib import admin
from .models import Operation, Category


# admin.site.register(Operation)

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'operation_at') 
    list_filter = ('operation_at',) 
    search_fields = ('name',) 
    ordering = ('-operation_at',) 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) 