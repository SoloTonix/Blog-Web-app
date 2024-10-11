from django import forms
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    #title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter body'}))
    #publish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model = Post
        fields = ['title', 'body', 'publish', 'image']

class CreateCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your comments...'}))
    class Meta:
        model = Comment 
        fields = ['text']



