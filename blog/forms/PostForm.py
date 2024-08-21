from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ("category", "title", "content", "is_published", "tags", "image")
        widgets = {
            "category":forms.Select(attrs={'class':'form-control'}),
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "content":forms.Textarea(attrs={'class':'form-control'}),
            # "author":forms.Select(attrs={'class':'form-control'}),
            "is_published":forms.CheckboxInput(attrs={'class':"form-check-input"}),
            "tags":forms.SelectMultiple(attrs={'class':'form-control'}),
            "image":forms.FileInput(attrs={'class':'form-control'}),
        }