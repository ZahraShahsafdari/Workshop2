from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class RequestSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, data):
        u = User(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            username = data['username'],
            password = data['password']
        )
        u.set_password(data['password'])
        u.save()
        return u
    
#-------------------------------------------------------------------------------

class RequestLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100, allow_blank = False)
    password = serializers.CharField(max_length = 100, allow_blank = False)

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.post('password')
        )
        return validated_data

    def validated_password(self, data):
        if data != request.data['password']:
            raise serializer.ValidationError(
                'Incorrest password, please try again!'
            ) 
        return data 

#-------------------------------------------------------------------------------

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

#-------------------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'last_login', 'password', 'user_permissions']