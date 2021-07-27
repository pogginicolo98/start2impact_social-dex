from django import forms
from posts.models import Post


class PostModelForm(forms.ModelForm):
    """
    A form class for new 'Post'.

    validations:
    - content: Prohibits the publication of any post that contains the word 'hack'.
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

    def clean(self):
        # data from the form is fetched using super function
        super(PostModelForm, self).clean()

        # extract the username and text field from the data
        content = self.cleaned_data.get('content')

        # conditions to be met for the username length
        if "hack" in content.lower():
            self._errors['content'] = self.error_class([
                "forbidden word: 'hack'"])

        # return any errors if found
        return self.cleaned_data
