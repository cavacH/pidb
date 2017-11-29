from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Tuser

def login(request):
    if request.method == 'POST':
        name = request.POST.get('user', None)
        password = request.POST.get('password', None)
        user = authenticate(username=name, password=password)
        if user is not None:
            question_list = user.tuser.question_set.all()
            q_name_list = []
            for question in question_list:
                q_name_list.append(question.name)
            return render(request, 'tabby/profile.html', {})
        else:
            return render(request, 'tabby/error.html', {})
    else:
        return render(request, 'tabby/login.html', {})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('user', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        user = authenticate(username=name, password=password)
        if user is None:
            new_user = User.objects.create_user(name, email, password)
            new_tuser = Tuser(user=new_user, status=0)
            new_tuser.save()
            return render(request, 'tabby/profile.html', {})
        else:
            return render(request, 'tabby/userExist.html', {})

