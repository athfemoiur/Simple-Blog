from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control'})}
