from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

class CreateProfileForm(UserCreationForm):
    email = forms.EmailField()
    favorite_color = forms.CharField(max_length=30)
    favorite_movie = forms.CharField(max_length=50)
    age = forms.IntegerField(validators=[MinValueValidator(limit_value=1)])

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'favorite_color', 'favorite_movie', 'age']
