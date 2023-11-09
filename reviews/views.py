from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Review

# Create your views here.

class ReviewListView(ListView):
    model = Review
    template_name = "home.html"


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviewDetail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ReviewDetailView, self).get_context_data(*args, **kwargs)
        context['review_list'] = Review.objects.all()
        return context