from django.urls import path
from .views import ReviewListView, ReviewDetailView

urlpatterns = [
    path("", ReviewListView.as_view(template_name="home.html"), name="home"),
    path("review/<int:pk>/", ReviewDetailView.as_view(template_name="reviewDetail.html"), name="review_detail"),
]
