from django.urls import path
from .views import (
    sticky_note_list,
    sticky_note_detail,
    sticky_note_create,
    sticky_note_update,
    sticky_note_delete,
)

app_name = "posts"

urlpatterns = [
    # URL pattern for displaying all of the sticky notes
    path("", sticky_note_list, name="sticky_note_list"),

    # URL pattern for displaying detail about a specific sticky note
    path("sticky_note/<int:pk>/", sticky_note_detail, name="sticky_note_detail"),

    # URL pattern for creating a new sticky note
    path("sticky_note/new/", sticky_note_create, name="sticky_note_create"),

    # URL pattern for updating an existing sticky note
    path("sticky_note/<int:pk>/edit/", sticky_note_update, name="sticky_note_update"),

    # URL pattern for deleting an existing sticky note
    path("sticky_note/<int:pk>/delete/", sticky_note_delete, name="sticky_note_delete"),
]
