from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Post

class CreatePostForm(forms.ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = Post
        fields = ['title', 'content']

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']