from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Review
from django.urls import reverse_lazy
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
    

class ReviewCreateView(CreateView):
    model = Review
    template_name = "reviewCreate.html"
    fields = ["movie", "thumbnail", "title", "content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "reviewUpdate.html"
    fields = ["thumbnail", "title", "content"]

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "reviewDelete.html"
    success_url = reverse_lazy('home')

