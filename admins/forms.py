from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(AdminUserCreationForm, self).save(commit=False)
        user.is_staff = True  # Set user as staff/admin
        if commit:
            user.save()
        return user
