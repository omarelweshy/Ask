from django.urls import path
from .views import *
urlpatterns = [
    path('inbox', InboxListView.as_view(), name='inbox')
]
