from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Person, Department, Office, Post
from .serializers import PersonSerialize, DepartmentSerialize, OfficeSerialize, PostSerialize
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from .permissions import PostViewersAuth


class PersonViewSet(viewsets.ModelViewSet):
    #Описываем объекты таблицы базы данных
    queryset = Person.objects.all()
    #Указываем сериализоватор для преобразовани данных
    serializer_class = PersonSerialize
    #Выбираем уровень доступа к данным (в данном случае только авторизованным пользователям)
    permission_classes = (permissions.IsAuthenticated,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerialize
    #permission_classes = (permissions.IsAuthenticated,)
    


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerialize
    #Устанавливаю разрешение дающее право RW всем авторизованным пользователям, а остальным только на чтение
    permission_classes = (permissions.IsAuthenticated,)
    #Указываю, что аутентификация выполняется с помощью токена
    authentication_classes = (authentication.TokenAuthentication,)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialize
    #Предоставляю доступ только админам или пользователям группы PostViewers
    permission_classes = (PostViewersAuth|permissions.IsAdminUser,)