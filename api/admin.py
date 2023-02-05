from django.contrib import admin
from .models import Person, Department, Post, Office
from rest_framework.authtoken.admin import TokenAdmin

#Настройка ручного создания токенов через админку Django
TokenAdmin.raw_id_fields = ['user']

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Post)
admin.site.register(Office)
