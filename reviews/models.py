from django.db import models
from django.conf import settings 
from django.urls import reverse

# Create your models here.

class Review(models.Model):
    movie = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255) #currently saved as a url address
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("review_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse("review_list")