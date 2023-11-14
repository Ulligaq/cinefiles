
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CreateProfileForm


# Create your views here.

class CreateProfileView(CreateView):
    template_name = 'userProfile/templates/createprofile.html'

    def get(self, request, *args, **kwargs):
        form = CreateProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')  # Import redirect here
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})

class EditProfileView(UpdateView):
    template_name = 'userProfile/templates/editprofile.html'

    def get(self, request, *args, **kwargs):
        form = UserChangeForm
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserChangeForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')  # Import redirect here
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})
    
    def get_object(self):
        return self.request.server