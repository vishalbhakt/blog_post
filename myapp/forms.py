from django import forms
from myapp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('author', 'Author'), ('admin', 'Admin')], required=True)

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]

