from django.db import models
from datetime import datetime
# Create your models here.
class Hunikappuser(models.Model):
    
    sessiondId = models.CharField(max_length=255, null=True)
    serviceCode = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.phoneNumber


# class Iteganyagihe(models.Model):
#     sessionId = models.CharField(max_length=255, null=True)
#     phonNumber = models.CharField(max_length=255)
#     category = models.CharField(max_length=255)

#     def __str__(self):
#         return self.phonNumber


# class Model(models.Model):
#     title = models.CharField(max_length=255,null=True)

#     def __str__(self):
#         return self.title

