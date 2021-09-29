from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout

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
    # bot(request, serialize('json', User.objects.all(), fields=('username'), cls=LazyEncoder))
    return render(request,'home.html')    

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')   

    if request.method == 'POST':
        print("--------------------")
        username = request.POST.get('username')
        password = request.POST.get('password')
        # password2 = request.GET['password']
        print("username", username)
        print("password", password)
        # print("password2", password2)
        usr = authenticate(request, username=username, password=password)
        print(usr)
        
        if usr is not None:
            auth_login(request, usr)
            return redirect('home')
        else:
            error = 'Invalid creditials ! !'
            print(error)
            return render(request, 'login.html', {'error':error})

def signup(request):
    if request.method == 'GET':
        # if request.user.is_authenticated:
        #     return redirect('home')
        # else:
        return render(request, 'signup.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            print("user succesfully created")
            user = User.objects.create(username=username, email=email, password=password)
            auth_login(request, user)
            return redirect('home')
        else:
            pwrd_error = "password did not match"
            print(pwrd_error)
            return render(request, 'signup.html', {'pword_error': pwrd_error})

    return render(request, 'signup.html')