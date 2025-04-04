from django import forms
from myapp.models import Post,ProfileUpdate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # role = forms.ChoiceField(choices=[('author', 'Author'), ('admin', 'Admin')], required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = ProfileUpdate
        fields = ["full_name","phone_number","profile_picture","bio","date_of_birth","gender","address","website"]

