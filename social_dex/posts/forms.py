from django import forms
from posts.models import Post


class PostModelForm(forms.ModelForm):
    """
    A form class for new 'Post'.
    """

    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'What are you thinking about?', 'rows': 5})
        }
        labels = {
            'content': False
        }
