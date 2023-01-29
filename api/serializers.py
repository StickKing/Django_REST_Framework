from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person, Department, Office, Post

class PersonSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        field = ['first_name', 'second_name', 'patronymic', 'birthday', 'email', 'in_vacation', 'department']

class DepartmentSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        field = ['name', 'telefon', 'email', 'office']