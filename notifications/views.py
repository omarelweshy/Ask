from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import *
from django.contrib.auth import get_user_model
from questions.models import Question


class InboxListView(ListView):
    model = Question
    template_name = "notifications/inbox.html"
