from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile', UserProfile.as_view(), name='profile'),

]
