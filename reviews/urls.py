from django.urls import path, include
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path("reviewCreate/", ReviewCreateView.as_view(template_name="reviewCreate.html"), name="review_create"),
    path("", ReviewListView.as_view(template_name="home.html"), name="home"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("review/edit/<int:pk>/", ReviewUpdateView.as_view(template_name="reviewUpdate.html"), name="review_update"),
    path("review/<int:pk>/delete", ReviewDeleteView.as_view(template_name="reviewDelete.html"), name="review_delete"),
    path("profile/", include("django.contrib.auth.urls")), #new url for users
    path("profile/", include("userProfile.urls")), #url  for profiles
]
