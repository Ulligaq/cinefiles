from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.core.validators import MinValueValidator


class CreateProfileForm(UserCreationForm):
    username = forms.CharField(
        max_length=15,
        help_text="Please do not make innapropriate names, username must be under or equal to 15 characters.",
    )

    email = forms.EmailField()

    favorite_color = forms.CharField(
        max_length=20, help_text="Can be changed in profile"
    )

    favorite_movie = forms.CharField(
        max_length=30, help_text="Can be changed in profile"
    )

    age = forms.IntegerField(validators=[MinValueValidator(limit_value=1)])

    class Meta:
        model = UserProfile

        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "favorite_color",
            "favorite_movie",
            "age",
        ]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = ["favorite_movie", "favorite_color"]
