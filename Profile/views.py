from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.base import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from .models import UserProfile
# Create your views here.

class Index(View):

    def get(self, request):
        if auth.get_user(request).is_authenticated:  # якщо користувач залогінений
            return redirect('home')  # редірект на домашню сторінку
        return render(request, 'index.html')  # якщо ні, редірект на головну сторінку

class Home(View):

    def get(self, request):
        return render(request, 'profile/home.html')

class ProfileView(View):
    """Вивід профіля користувача"""
    def get(self, request, username):
        if username == request.user.username: #якшо юзернейм == юзернейму залогіненому
            user = UserProfile.objects.get(username=username)
            context = {'user': user}
            return render(request, 'profile/profile.html', context)
        else:
            return redirect('/')




class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'authentication/login.html', context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username, password=password
            )
            if user:
                login(request, user)
                return redirect('home')

        context = {
            'form': form,
        }
        return render(request, 'authentication/login.html', context)

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'authentication/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(
                username=new_user.username, password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'authentication/registration.html', context)
