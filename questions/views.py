from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import *
from django.contrib.auth import get_user_model
from .models import Question


class QuestionsListView(ListView):
    model = Question
    context_object_name = 'questions'
    paginate_by = 5
    template_name = "notifications/questions.html"
