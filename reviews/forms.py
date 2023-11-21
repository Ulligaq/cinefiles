from django import forms
from .models import Comment, Review

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'commentContent'}),
        }
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("movie", "thumbnail", "title", "content")
        widgets = {
            'content': forms.Textarea(attrs={'class': 'reviewContent'}),
            'title': forms.TextInput(attrs={'class': 'reviewContent'}),
            'movie': forms.TextInput(attrs={'class': 'reviewThin'}),
            'thumbnail': forms.TextInput(attrs={'class': 'reviewThin'}),
        }
        