from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import Profile
from .forms import CreateUserForm, EditProfileForm
from django.urls import reverse_lazy


class CreateUserView(CreateView):
    template_name = "createprofile.html"
    form_class = CreateUserForm
    success_url = "/profile/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profileoverview.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        # Try to get the user's profile; create it if it doesn't exist
        profile, created = Profile.objects.get_or_create(user=self.request.user)

        return profile


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy(
        "profileoverview"
    )  # Assuming you have a URL pattern named 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        # Set the user for the profile before saving
        form.instance.user = self.request.user
        return super().form_valid(form)
