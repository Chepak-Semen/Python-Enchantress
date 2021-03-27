from django.contrib import admin

# Register your models here.
from apps.users.models import TrelloUser

admin.site.register(TrelloUser)
