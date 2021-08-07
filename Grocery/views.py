from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from Grocery.login import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def get(self, request, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('grocery:index')
        return render(request, self.template_name, {"form": form})


class RegisterView(FormView):
    form_class = LoginForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('grocery:index')


class LogoutView(View):

    def get(self, request):
        logout(request)
        print("logged out successfully")
        return redirect('login')
