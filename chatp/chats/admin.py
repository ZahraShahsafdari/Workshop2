from django.contrib import admin
from chats.models import Conversations, Messages

class MessageAdmin(admin.ModelAdmin):
    list_display = ('text' , 'sender' , 'date' , 'status',)
    search_fields = ('text',)

admin.site.register(Conversations)
admin.site.register(Messages, MessageAdmin)