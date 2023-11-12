from django.urls import path
from .views import CreateProfileView

urlpatterns = [


    path("new-user/", CreateProfileView.as_view(), name="createprofile"), #url for new user profile creation




]