from django.shortcuts import render, get_object_or_404, redirect
from .models import Sticky_note
from .forms import PostForm
import random


def sticky_note_create(request):
    """
    View to create a new sticky note.

    Parameters:
    - request: HTTP request object.
    - return: Rendered template for creating sticky note
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("posts:sticky_note_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/sticky_note_form.html", {"form": form})


def sticky_note_detail(request, pk):
    """
    View to display details of a specific sticky note.

    Parameters:
    - request: HTTP request object.
    - pk: Primary key of the sticky note to retrieve.

    Returns:
    - Rendered template displaying sticky note details.
    """
    sticky_note = get_object_or_404(Sticky_note, pk=pk)
    return render(request, "posts/sticky_note_detail.html", {"sticky_note": sticky_note})


def sticky_note_list(request):
    """
    View to list all sticky notes.

    Parameters:
    - request: HTTP request object.

    Returns:
    - Rendered template displaying a list of sticky notes.
    """
    sticky_notes = Sticky_note.objects.all()

    # List of random colours
    colors = [
        '#FFCDD2', '#F8BBD0', '#E1BEE7',
        '#D1C4E9', '#C5CAE9', '#BBDEFB',
        '#B2EBF2', '#B2DFDB', '#C8E6C9',
        '#DCEDC8', '#FFF9C4', '#FFECB3'
    ]
    notes_with_colors = []
    # Assign random colour to a note
    for note in sticky_notes:
        color = random.choice(colors)
        notes_with_colors.append((note, color))

    return render(request, "posts/sticky_note_list.html",
                  {"notes_with_colors": notes_with_colors, "page_title": "Sticky Notes"})


def sticky_note_update(request, pk):
    """
    View to update an existing sticky note.

    Parameters: Http request object
    pk: Primary key of the sticky note
    return: Rendered template for updating the note
    """
    sticky_note = get_object_or_404(Sticky_note, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=sticky_note)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("posts:sticky_note_detail", pk=sticky_note.pk)
    else:
        form = PostForm(instance=sticky_note)
    return render(request, "posts/sticky_note_form.html", {"form": form})


def sticky_note_delete(request, pk):
    """
    View to delete a sticky note.

    Parameters:
    - request: HTTP request object.
    - pk: Primary key of the sticky note to delete.
    Returns: Redirect to the sticky note list view after deletion.

    """
    post = get_object_or_404(Sticky_note, pk=pk)
    post.delete()
    return redirect("posts:sticky_note_list")
