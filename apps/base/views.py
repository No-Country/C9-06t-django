from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.accounts.decorators import allowed_users

# Create your views here.


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['user'])
def home(request):
    context = {}

    return render(request, 'index.html', context)
