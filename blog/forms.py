from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Creates a new comment form object to be called by the PostDetail view
    """
    class Meta:
        model = Comment
        fields = ['body']
