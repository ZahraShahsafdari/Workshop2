from rest_framework import serializers
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from chats.models import Messages, Conversations


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

#-------------------------------------------------------------------------------

class ConversationSerializer(serializers.ModelSerializer):
    members = UsersSerializer(many = True)
    class Meta:
        model = Conversations
        fields = ['name', 'members']   

#-------------------------------------------------------------------------------

class UpdateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'text']

#-------------------------------------------------------------------------------

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['conversation','text']
