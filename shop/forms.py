from django import forms
from django.forms import fields
from shop.models import Comment

class CommentForm(forms.ModelForm):
    comment_body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
        'rows':'3',
        'placeholder':'Write your comment on this post .....'
        }))
    comment_author = forms.CharField(
        label='',
        widget = forms.CharField(
            attrs={
                'row':1,
                'placeholder':"Let's know your name"
            }
        )
    )
    class Meta:
        model = Comment
        fields = ['comment_author','comment_body']