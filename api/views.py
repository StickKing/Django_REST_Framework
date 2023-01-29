from django.shortcuts import render
from .models import Person, Department, Office, Post
from .serializers import PersonSerialize, DepartmentSerialize
from rest_framework import viewsets
from rest_framework import permissions

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerialize
    permission_classes = [permissions.IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerialize
    permission_classes = [permissions.IsAuthenticated]

