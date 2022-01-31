from django.contrib import admin
from .models import *  #importing all models
# Register your models here.

class HunikappuserAdmin (admin.ModelAdmin):
    list_display =['phoneNumber']
    search_fields =['phoneNumber']

# class IteganyagiheAdmin (admin.ModelAdmin):
#     list_display = ['phonNumber', 'category']
#     search_fields = ['phonNumber', 'category']


# admin.site.register(hunikappuser, hunikappAdmin)
# admin.site.register(Iteganyagihe, IteganyagiheAdmin)
admin.site.register(Hunikappuser, HunikappuserAdmin )