from .models import User, UserProfile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.


class signup(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'userprofile/signup.html', {'form' : form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            userprofile = UserProfile.objects.create(user = user)

            login(request, user)

            return redirect('frontpage')




