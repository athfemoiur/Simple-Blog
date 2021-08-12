from django import forms
from django.forms import ModelForm

from category.models import Category
from post.models import Post


class PostForm(ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'categories', 'attachment', 'status')
