from django.urls import path
from .views import CreateProfileView, EditProfileView, ProfileOverviewView

urlpatterns = [
    path(
        "new-user/",
        CreateProfileView.as_view(template_name="createprofile.html"),
        name="createprofile",
    ),  # url for new user profile creation
    path(
        "edit/",
        EditProfileView.as_view(template_name="editprofile.html"),
        name="edit_profile",
    ),
    path(
        "overview/",
        ProfileOverviewView.as_view(template_name="profileoverview.html"),
        name="profileoverview",
    ),
]
