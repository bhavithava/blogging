from django.shortcuts import render, redirect

# Create your views here.
def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def mainhomepage(request):
    return render(request, 'mainhomepage.html')

def userhomepage(request):
    return render(request, 'userhomepage.html')

def signup(request):
    return render(request, 'signup.html')

from django.contrib import messages
from django.contrib.auth.models import User,auth

'''
def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'projecthomepage.html')
        else:
            messages.info(request, 'Passwords do no match')
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')
'''


def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup1')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mainhomepage')  # Assuming mainhomepage is the target after successful login
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'projecthomepage.html')

