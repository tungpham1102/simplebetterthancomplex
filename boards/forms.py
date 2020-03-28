from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        max_length=4000,
        widget=forms.Textarea(attrs={
            'row': 5,
            'placeholder': 'What is on your mind',
        }),
        help_text='The max length of the text is 4000'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['message']