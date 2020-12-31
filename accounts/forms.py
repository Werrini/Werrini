from django.db import models
from django.utils.translation import ugettext_lazy as _
from allauth.account.forms import SignupForm
from django_countries.fields import CountryField

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    password2 = None
    class Meta:
        model = get_user_model()
        fields = ['full_name','country', 'email']
    def clean_password2(self):
        password2 = None
