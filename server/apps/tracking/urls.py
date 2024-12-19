from django.urls import path

from rest_framework import routers, permissions
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import index, CategoryViewSet, OperationViewSet
from .views import MyTokenObtainPairView

router = routers.DefaultRouter()

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
operation_list = OperationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
operation_detail = OperationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = 'tracking'

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
        terms_of_service="<https://www.google.com/policies/terms/>",
        contact=openapi.Contact(email="contact@api.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', index, name='index'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('operations/', operation_list, name='operation-list'),
    path('operations/<int:pk>/', operation_detail, name='operation-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
