
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CreateProfileForm
from reviews.models import Review
from .models import Profile


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
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        reviews = Review.objects.filter(author=pk)


        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request, "profile.html", {"profile":profile, "reviews":reviews})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page"))
        return redirect('home')
                        
class EditBioView(UpdateView):
    model = Profile
    template_name = 'profiles/profileEditBio.html'
    fields = ["biography",]

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.profile.pk + 1})

    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def get_form(self, form_class=None):
        form = super(EditBioView, self).get_form(form_class)
        form.fields['biography'].widget.attrs['class'] = 'reviewContent'
        return form
