from django import forms
#from .models import ViewFilters, Fungi, ShowAllData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import DataFilter
from .models import Profile
#from .models import ViewFiltersb


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email']	

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['user','image']




		