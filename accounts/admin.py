from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomChangeForm, CustomCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomCreationForm
    form = CustomChangeForm
    list_display = ('email', 'username',)


admin.site.register(CustomUser, CustomUserAdmin)
