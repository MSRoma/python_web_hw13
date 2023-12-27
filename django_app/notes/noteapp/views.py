from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm ,NoteForm, AuthorForm
from .models import Tag, Note , Author


from itertools import count
from django.core.management.base import BaseCommand
import json
from noteapp.models import Tag, Author, Note
import datetime
from datetime import datetime


# Create your views here.
def main(request, tag = 0):
    if request.method != 'POST':
        print(request.POST)
        notes = Note.objects.all()
        tags = Tag.objects.filter().order_by()[:10]

    else:
        print(request.POST)
        notes = Note.objects.all()
        tags = Tag.objects.filter().order_by()[:10]
        
    paginator = Paginator(notes, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


#users = User.objects.filter(  # WHERE    first_name='John',).order_by(  # ORDER BY    '-last_name')[:10]  # LIMIT


    return render(request, 'noteapp/index.html', {"page_obj": page_obj,"tags": tags})

#@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})
   
    return render(request, 'noteapp/tag.html', {'form': TagForm()})

#@login_required
def note(request):
    # tags = Tag.objects.filter(user=request.user).all()
    # authors = Author.objects.filter(user=request.user).all()
    # tags = Tag.objects.all()
    # authors = Author.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            print(f"NOTE FORM valid")
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/note.html', {'form': form})
    
    return render(request, 'noteapp/note.html', {'form': NoteForm()})

@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            print(f"AUTHOR FORM valid")
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/author.html', {'form': form})
    
    return render(request, 'noteapp/author.html', {'form': AuthorForm()})

#@login_required
def detail(request, note_id ):

    author_ = Author.objects.get(id=note_id)

   # author = get_object_or_404(Author, pk=author_id)
    return render(request, 'noteapp/detail.html', {"author": author_ })

@login_required
def set_done(request, note_id):
    Note.objects.filter(pk=note_id, user=request.user).update(done=True)
    return redirect(to='noteapp:main')

@login_required
def delete_note(request, note_id):
    Note.objects.get(pk=note_id, user=request.user).delete()
    return redirect(to='noteapp:main')

@login_required
def profile(request):
    return render(request, 'users/profile.html')