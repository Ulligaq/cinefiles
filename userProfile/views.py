from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CreateProfileForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "userProfile/templates/createprofile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy(
        "profile/new-user/"
    )  # Change this to the desired success URL

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        user_profile = form.save(commit=False)
        user_profile.user = user
        user_profile.save()
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditProfileView(UpdateView):
    model = UserProfile
    template_name = "userProfile/templates/editprofile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy(
        "profile/edit/"
    )  # Change this to the desired success URL

    def get_object(self, queryset=None):
        return self.request.user


class ProfileOverviewView(DetailView):
    model = UserProfile
    template_name = "userProfile/templates/profileoverview.html"
    context_object_name = "user_profile"
    success_url = reverse_lazy("profile/edit/")

    def get_object(self, queryset=None):
        return self.request.user
