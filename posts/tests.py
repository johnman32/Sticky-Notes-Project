from django.test import TestCase
from django.urls import reverse
from .models import Sticky_note, Author


class Sticky_noteModelTest(TestCase):
    def setUp(self):
        # Creates a note object for testing
        author = Author.objects.create(name="Test Author")
        Sticky_note.objects.create(title='Test Note', content='This is a test note', author=author)

    def test_sticky_note_has_title(self):
        # Tests that note title is correct
        sticky_note = Sticky_note.objects.get(id=1)
        self.assertEqual(sticky_note.title, 'Test Note')

    def test_sticky_note_has_content(self):
        # Tests that content title is correct
        sticky_note = Sticky_note.objects.get(id=1)
        self.assertEqual(sticky_note.content, "This is a test note")


class Sticky_noteViewTest(TestCase):
    def test_sticky_note_create(self):
        # Test GET request for create URL
        response = self.client.get(reverse("posts:sticky_note_create"))
        self.assertEqual(response.status_code, 200)

        # Test POST request
        note_data = {
            "title": "Test Note",
            "content": "This is a test note",
        }
        response = self.client.post(reverse("posts:sticky_note_create"), note_data)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Sticky_note.objects.count(), 1)
        new_note = Sticky_note.objects.first()
        self.assertEqual(new_note.title, "Test Note")
        self.assertEqual(new_note.content, "This is a test note")

    def test_sticky_note_view(self):
        # Test GET request for view URL
        response = self.client.get(reverse("posts:sticky_note_list"))
        self.assertEqual(response.status_code, 200)


class Sticky_noteEditTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author', email="test@email.com")
        self.sticky_note = Sticky_note.objects.create(
            title="Original Title",
            content="Original content",
            author=self.author
        )

    def test_sticky_note_update(self):
        # Test GET request for create URL
        url = reverse("posts:sticky_note_update", args=[self.sticky_note.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Original Title")
        self.assertContains(response, "Original content")

        # POST request to change note
        note_data = {
            "title": "Updated title",
            "content": "Updated content"
        }
        response = self.client.post(url, note_data)
        self.assertEqual(response.status_code, 302)

        # Checks object has changed title/content
        self.sticky_note.refresh_from_db()
        self.assertEqual(self.sticky_note.title, "Updated title")
        self.assertEqual(self.sticky_note.content, "Updated content")

    def test_sticky_note_delete(self):
        # Test GET request for delete URL
        url = reverse("posts:sticky_note_delete", args=[self.sticky_note.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # Checks to see if note is removed
        note_exists = Sticky_note.objects.filter(pk=self.sticky_note.pk).exists()
        self.assertFalse(note_exists)
