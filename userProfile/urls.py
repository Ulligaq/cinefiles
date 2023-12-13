from django.urls import path
from .views import CreateProfileView, EditBioView
from . import views

urlpatterns = [
    path("new-user/", CreateProfileView.as_view(template_name="createprofile.html"), name="createprofile"), #url for new user profile creation
    path("profile/<int:pk>", views.profile, name='profile'),
    path('profileEditBio/', EditBioView.as_view(template_name="profileEditBio.html"), name='profileEditBio'),
]