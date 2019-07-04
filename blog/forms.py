from __future__ import absolute_import
from django import forms
from mdeditor.fields import MDTextFormField
from .models import Post, Comment


CATEGORY_CHOICES = Post.CATEGORY_CHOICES
LEVEL_CHOICES = Post.LEVEL_CHOICES


class MDEditorForm(forms.Form):
    title = forms.CharField()
    synopsis = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="category", initial='', widget=forms.Select())
    level = forms.ChoiceField(choices=LEVEL_CHOICES, label="level", initial='', widget=forms.Select())
    content = MDTextFormField()


class MDEditorModleForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)