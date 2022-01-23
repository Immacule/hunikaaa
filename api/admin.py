from django.contrib import admin
from  .models import *
# Register your models here.
class FarmersAdmin(admin.ModelAdmin):
    list_display =['fullname', 'phone', 'email']
admin.site.register(Farmers, FarmersAdmin)
admin.site.register(Profile)