from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Farmers(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username= models.CharField(max_length=255)
    district=models.CharField(max_length=244)
    accountType=models.CharField(max_length=255)

    def __str__(self):
        return self.username 


class Agronome(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname