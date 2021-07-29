from django import forms
from posts.models import Post


class PostModelForm(forms.ModelForm):
    """
    A form class for create new 'Post'.

    validations:
    - content: The word 'hack' is forbidden.
    """

    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your post on the blockchain...', 'rows': 5})
        }
        labels = {
            'content': False
        }

    def clean(self):
        # data from the form is fetched using super function
        super(PostModelForm, self).clean()

        # extract the username and text field from the data
        content = self.cleaned_data.get('content')

        # conditions to be met for the username length
        if content and "hack" in content.lower():
            self._errors['content'] = self.error_class([
                "Forbidden word: 'hack'"])

        # return any errors if found
        return self.cleaned_data
