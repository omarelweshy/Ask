from django.urls import path
from .views import *
urlpatterns = [
    path('questions', QuestionsListView.as_view(), name='questions')
]
