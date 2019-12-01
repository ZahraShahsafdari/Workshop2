from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User
from users.views import UserSerializer
from chats.models import Messages, Conversations
from chats.serializers import UsersSerializer, ConversationSerializer, UpdateMessageSerializer, MessagesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from PIL import Image
from django.http import JsonResponse



class ConversationView(APIView):
    authentication_classes = []
    def post(self, request):
        c = ConversationSerializer(
        Conversations.objects.all()
        , many = True
        )
        return JsonResponse(
            {
            'conversations': c.data
            }
        ) 

    def get(self, request):
        authentication_classes = []
        s = ConversationSerializer(
            Conversations.objects.all(),
            many = True
        )
        return JsonResponse({
            'conversations': s.data
        })


#-------------------------------------------------------------------------------

class MessageView(APIView):
    authentication_classes = []
    def post(self, request):
        if request.method != 'POST':
            return JsonResponse(
                {
                'message': 'Method is not allowed!'
                },
            status = status.HTTP_405_METHOD_NOT_ALLOWED
            )  
             
        m = MessagesSerializer(
            Messages.objects.all()
            , many = True
            )
        return Response(m.data)
        

    def put(self, request):
        m = UpdateMessageSerializer(
            instance = Messages.objects.get(
                id = request.data['id']
            ),
            data = request.data     
        )
        if m.is_valid():
            m.save() 
            return Response(
                {
                'message': 'Message was updated successfully!'
                }
            )
        else:  
            return Response(
                {
                    'errors': m.errors
                },
                status = status.HTTP_400_BAD_REQUEST
            )  
    

    def get(self, request):
        if request.method != 'GET':
            return JsonResponse(
                {
                'message': 'Method is not allowed!'
                }, 
            status = status.HTTP_405_METHOD_NOT_ALLOWED)  

        elif 'conversation' not in request.GET:
            return JsonResponse(
                {
                'message': 'Not found!'
                },
            status = status.HTTP_400_BAD_REQUEST)    

        c = Conversations.objects.get(
            id = request.GET['conversation']
        )
        messages = Messages.objects.filter(
            conversation = c
        )
        s = MessagesSerializer(
            messages, 
            many = True
            )
        return JsonResponse(
            {
            'messages': s.data
            }
        ) 
   