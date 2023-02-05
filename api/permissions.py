from rest_framework import permissions
from rest_framework.permissions import (DjangoModelPermissions)


class PostViewersAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        #Если пользователь авторизован и принадлежит группк PostViewers доступ будет разрешён
        return request.user.is_authenticated and request.user.groups.filter(name='PostViewers').exists()

