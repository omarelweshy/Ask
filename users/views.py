from .forms import *
from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from .models import User


class ProfileSettingsUpdateView(UpdateView):
    model = User
    form = UserChangeForm
    fields = ['first_name', 'last_name', 'location',
              'bio', 'url', 'photo', 'gender']
    template_name = "profile_settings/profile_settings.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class AccountSettingsUpdateView(UpdateView):
    model = User
    form = UserChangeForm
    fields = ['username', 'email', ]
    template_name = "profile_settings/account_settings.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
