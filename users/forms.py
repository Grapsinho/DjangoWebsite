from playground.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'password1', 'password2', 'email']

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']