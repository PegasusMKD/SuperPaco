from django.contrib import admin

# Register your models here.
from .models import ID, Leftovers

admin.site.register(ID)
admin.site.register(Leftovers)