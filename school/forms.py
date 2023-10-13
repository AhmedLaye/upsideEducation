from logging import PlaceHolder
from django import forms
from .models import *

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='',widget=forms.TextInput(attrs={'placeholder': "Nom d'ulilisateur"}))
    password = forms.CharField(max_length=63,label='', widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cour
        fields = ['titre','chapitre', 'contenu']

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')