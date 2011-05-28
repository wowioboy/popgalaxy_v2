from django import forms
from comments.models import *

class CommentForm(forms.ModelForm):
    
    class Meta:

        model = Comment
        exclude = ('author',) 