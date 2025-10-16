from django.db import models


class Sticky_note(models.Model):
    """Model representing a sticky note.
    Fields:
    - title: The title of the sticky note.
    - content: The main content/body of the sticky note.
    - created_at: Timestamp when the note was created.
    - updated_at: Timestamp when the note was last updated.

    Methods:
    -__str__: Returns a string representation of the sticky note.

    Parameters:
    -models.Model: Inherits from Django's base model class.

    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    """Model representing an author of sticky notes.
    Fields:
    - name: The name of the author.
    - email: The email address of the author.

    Methods:
    - __str__: Returns a string representation of the author.

    Parameters:
    - models.Model: Inherits from Django's base model class.

    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
