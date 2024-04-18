from django.contrib import admin
from .models import Item, CustomUser, Whole

admin.site.register(Item)
admin.site.register(CustomUser)
admin.site.register(Whole)

