from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from webapp.models import Record

# Register/Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2']
        

# Login User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Create Records

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"


# Update Records

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"



