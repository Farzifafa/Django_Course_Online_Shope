from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomCreationForm(UserCreationForm):
    model = get_user_model()
    field = ('email', 'username',)


class CustomChangeForm(UserChangeForm):
    model = get_user_model()
    field = ('email', 'username',)
