from django.contrib import admin
from .models import Person, Department, Post, Office

admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Post)
admin.site.register(Office)
