from django import forms
from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import TextInput, Textarea


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'is_published', 'hide_description', 'created_at')
    list_editable = ('title', 'is_published', 'hide_description')
    readonly_fields = ('created_at',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        RichTextField: {'widget': Textarea(attrs={'rows':4, 'cols':50})},
    }

admin.site.register(Post, PostAdmin)