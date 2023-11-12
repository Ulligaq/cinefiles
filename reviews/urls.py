from django.urls import path, include
from .views import ReviewListView, ReviewDetailView, ReviewCreateView

urlpatterns = [
    path("review/create/", ReviewCreateView.as_view(template_name="reviewCreate.html"), name="review_create"),
    path("", ReviewListView.as_view(template_name="home.html"), name="home"),
    path("review/<int:pk>/", ReviewDetailView.as_view(template_name="reviewDetail.html"), name="review_detail"),
    path("profile/", include("django.contrib.auth.urls")), #new url for users
    path("profile/", include("userProfile.urls")), #url  for profiles
]
