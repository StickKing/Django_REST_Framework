from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import PersonViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'department', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]