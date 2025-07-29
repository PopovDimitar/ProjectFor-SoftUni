from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteUploadForm, CustomRegisterForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import FileResponse, Http404
from .models import Note

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteUploadForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('/')
    else:
        form = NoteUploadForm()
    return render(request, 'upload_note.html', {'form': form})

def browse_notes(request):
    query = request.GET.get('q')
    sort = request.GET.get('sort', 'newest')

    notes = Note.objects.all()

    if query:
        notes = notes.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query) |
            Q(subject__icontains=query)
        )

    if sort == 'newest':
        notes = notes.order_by('-id')
    elif sort == 'oldest':
        notes = notes.order_by('id')
    elif sort == 'az':
        notes = notes.order_by('title')
    elif sort == 'za':
        notes = notes.order_by('-title')

    return render(request, 'browse_notes.html', {'notes': notes})


def download_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        note.downloads += 1
        note.save()
        return FileResponse(note.file.open('rb'), as_attachment=True)
    except Note.DoesNotExist:
        raise Http404("Note not found")



def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def view_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'view_note.html', {'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('/')

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'POST':
        form = NoteUploadForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('view_note', note_id=note.id)
    else:
        form = NoteUploadForm(instance=note)

    return render(request, 'edit_note.html', {'form': form, 'note': note})