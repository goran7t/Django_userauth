from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    auth = True
    if not request.user.is_authenticated():
        auth = False
    return render(request, 'index.html', {'auth':auth})

def sign