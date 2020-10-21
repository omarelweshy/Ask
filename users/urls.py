from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/', ProfileSettingsUpdateView.as_view(),
         name='settings_profile'),
    path('account/', AccountSettingsUpdateView.as_view(),
         name='settings_account'),

]
