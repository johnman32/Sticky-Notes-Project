from django import forms
from .models import Sticky_note


class PostForm(forms.ModelForm):
    """
    Form to create and update post objects.

    Fields:
    - title: The title of the sticky note.
    - content: The main content/body of the sticky note.

    Meta class:
    - defines mode to use (Post) and fields to include in the form.
    """

    class Meta:
        model = Sticky_note
        fields = ['title', 'content', 'author']
