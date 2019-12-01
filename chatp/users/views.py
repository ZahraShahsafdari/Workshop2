from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import RequestSignupSerializer, RequestLoginSerializer, UpdateProfileSerializer, UserSerializer
from django.http import JsonResponse


class SignupView(APIView):
    authentication_classes = []
    def post(self, request):
        s = RequestSignupSerializer(data = request.data)
        if s.is_valid():
            u = s.save()
            return Response({
                'message': 'Account was created successfuly',
                'data': s.data
            })
        return Response(
            s.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

#-------------------------------------------------------------------------------

class LoginView(APIView):
    authentication_classes = []
    def post(self, request):
        s = RequestLoginSerializer(data = request.data)
        if s.is_valid():
            u = authenticate(
                request,
                username = s.data['username'],
                password = s.data['password']
                )
            if u is None:
                return Response(
                    {
                        'message': 'User was not found, please signup first!'
                    },
                    status = status.HTTP_404_NOT_FOUND
                ) 
            if u:
                login(request, u)
                return Response(
                    {
                        'data': {
                            "id": u.id,
                            'first_name': u.first_name,
                            'last_name': u.last_name,
                            'email': u.email,
                            'username': u.username,
                            'password': u.password
                        }
                    })
        else:
            return Response(
                s.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

#-------------------------------------------------------------------------------

class ProfileView(APIView):
    authentication_classes = []
    def put(self, request):
            s = UpdateProfileSerializer(
                instance = User.objects.get(id = request.data['id']),
                data = request.data,)
            if s.is_valid():
                s.save()
                return Response({
                    "message": "Your profile was updated successfully!"})
            else:
                return Response({"errors": s.errors})
                
#-------------------------------------------------------------------------------

class UserList(APIView):
    authentication_classes = []
    def get(self, request):
            u = UserSerializer(
            User.objects.all(),
            many = True)
            return JsonResponse(
                {
                'Users List': u.data
                })  