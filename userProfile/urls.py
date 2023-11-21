from django.urls import path, include
from .views import UserProfileView, CreateUserView, EditProfileView

urlpatterns = [
    path(
        "new-user/",
        CreateUserView.as_view(template_name="createprofile.html"),
        name="createprofile",
    ),  # url for new user profile creation
    path(
        "edit/",
        EditProfileView.as_view(template_name="editprofile.html"),
        name="edit_profile",
    ),
    path(
        "overview/",
        UserProfileView.as_view(template_name="profileoverview.html"),
        name="profileoverview",
    ),
]
