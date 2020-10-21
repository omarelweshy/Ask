from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _
from django.forms import ModelForm
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email',)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
