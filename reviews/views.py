from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from .models import Review
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
# Create your views here.

class ReviewListView(ListView):
    model = Review
    template_name = "home.html"

class CommentGet(DetailView):
    model = Review
    template_name = 'reviewDetail.html'
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        context['review_list'] = Review.objects.all()
        context['form'] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Review
    form_class = CommentForm
    template_name = "review_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.review = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        review = self.get_object()
        return reverse("review_detail", kwargs={"pk": review.pk})

class ReviewDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    

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

