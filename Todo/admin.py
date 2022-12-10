from django.contrib import admin

from Todo.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)