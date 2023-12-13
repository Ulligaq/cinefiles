from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

class CreateProfileForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'profileThin'}))
    favorite_color = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'profileThin'}))
    favorite_movie = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'profileThin'}))
    age = forms.IntegerField(validators=[MinValueValidator(limit_value=1)], widget=forms.NumberInput(attrs={'class': 'profileThin'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'favorite_color', 'favorite_movie', 'age')

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'profileThin'})