from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person, Department, Office, Post

#Создаю сериализатов модели Person
class PersonSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'patronymic', 'birthday', 'email', 'in_vacation', 'department']

#Создаю сериализатов модели Department 
class DepartmentSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'telefon', 'email', 'office']

#Создаю сериализатов модели Office
class OfficeSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = ['name']

class PostSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        ordering = ['-id']
        fields = ['name', 'salary', 'person']

