from django.db.models import fields
from rest_framework import serializers
from ussd.models import *
from .models import *
from django.contrib.auth.hashers import make_password

class FarmersSerializer(serializers.ModelSerializer):
    class Meta :
        model = Farmers
        depth=1
        fields = ('__all__')

class AgronomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agronome
        fields =('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields =('__all__')
        extra_kwargs={'user':{'required':False}
        }

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    class Meta:
        model=User
        depth=1
        fields = ('username','email', 'profile','password', 'first_name','last_name')
    def create(self, validated_data):
        email = validated_data['email']
        password =make_password(validated_data['password'])
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        
        username = validated_data['username']
        userInsert = User.objects.create(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # send message on email
        profile_data = validated_data.pop('profile')
        username= profile_data['username']
        district=profile_data['district']
        accountType=profile_data['accountType']
        profile= Profile.objects.create(
            user=userInsert,
            username=username,
            accountType=accountType,
            district=district
        )
        return userInsert