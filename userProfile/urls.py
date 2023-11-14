from django.urls import path
from .views import CreateProfileView

urlpatterns = [


    path("new-user/", CreateProfileView.as_view(template_name="createprofile.html"), name="createprofile"), #url for new user profile creation




]