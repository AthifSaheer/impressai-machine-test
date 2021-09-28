from django.shortcuts import render
from django.http import HttpResponse

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.conf import settings
# from ipware.ip import get_ip
import telegram
import requests


URL = settings.BOT_URL
token = settings.BOT_TOKEN
chat_id = settings.BOT_CHAT_ID

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, dict):
            return str(self.obj)
        return super().default(obj)

def bot(request, message, chat_id=chat_id, token=token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

def home(request):
    # if request.user:
    #     bot(request, str(get_ip(request)))
    # else:
    bot(request, serialize('json', User.objects.all(), fields=('username'), cls=LazyEncoder))
    
    smile_emoji = '\U0001F60D'
    html = "Hai, Your message has been sent.", smile_emoji
    return HttpResponse(html)
        
