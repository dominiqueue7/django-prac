from post.models import Post
from django.views.generic import ListView 
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))