from django.contrib import admin

from LIstings.models import IungoUser
from . import models
# Register your models here.

class IungoUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','first_name','last_name','ClientType','client_category']

admin.site.register(IungoUser,IungoUserAdmin)
