from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your views here.

def join_chat(request, username):
    return render(request, 'chat/join_chat.html', context={'username_json': mark_safe(json.dumps(username))})


def new_message(request, username):
    receiver = request.GET.get('receiver')
    text = request.GET.get('text')
    channel_layer = get_channel_layer()
    group_name = f"chat_{receiver}"
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'chat_message',
            'message': json.dumps({'sender': username, 'receiver': receiver, 'text': text})
        }
    )
    return HttpResponse('Message sent')
