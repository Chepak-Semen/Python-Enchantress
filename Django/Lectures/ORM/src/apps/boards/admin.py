from django.contrib import admin

# Register your models here.
from apps.boards.models import Board, Task, Comments

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(Comments)
