from django import forms

from .models import Post
from taggit.models import Tag


class PostForm(forms.ModelForm):
    title = forms.CharField()
    title.widget.attrs.update({'class': 'form-control border-0', 'style': 'background: transparent'})

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['title'].widget.attrs['readonly'] = True

    def clean_title(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.title
        else:
            return self.cleaned_data['title']
    
    
    class Meta:
        model = Post
        fields = ['title']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']