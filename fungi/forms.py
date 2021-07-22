from django import forms
from .models import Fungi
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FungiForm(forms.ModelForm):
		class Meta:
			model = Fungi
			fields  = "__all__"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserSearchForm(forms.Form):
    pass
