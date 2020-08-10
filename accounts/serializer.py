from django.contrib.auth import authenticate
from rest_framework import exceptions
from rest_framework import serializers

from django.contrib.auth import get_user_model

#https://www.youtube.com/watch?v=htPYk6QxacQ


from.models import *



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user=get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return  user

    class Meta:
        model=get_user_model()
        fields=('username','password')





class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    def validate(self, data):
        username=data.get("username","")
        password=data.get("password","")
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user

                else:
                    msg="user is deactivated"
                    raise  exceptions.ValidationError(msg)

            else:
                msg="unable to login with given crediants"
                raise  exceptions.ValidationError(msg)
        else:
            msg="Must provide username and password both"
            raise exceptions.ValidationError(msg)

        return data



