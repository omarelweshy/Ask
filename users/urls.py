from django.urls import path, include
from .views import *

urlpatterns = [
    path('settings/profile/', ProfileSettingsUpdateView.as_view(),
         name='settings_profile'),
    path('settings/account', AccountSettingsUpdateView.as_view(),
         name='settings_account'),
    path('profile', UserProfile.as_view(), name='profile'),

]
