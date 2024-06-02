from django.contrib import admin
from .models import Mymodel

# Register your models here.
@admin.register(Mymodel)
class myAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'sub', 'msg']
