from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import *
from users.forms import *
from posts.models import *
from .forms import *
from django.contrib.auth import get_user_model


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = "account_login"


class UserProfile(TemplateView):
    model = User
    context_data_name = 'user'
    template_name = "user_profile.html"
    slug_field = "username"
