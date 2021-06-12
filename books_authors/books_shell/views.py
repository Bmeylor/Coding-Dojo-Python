from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request,"index.html", context)

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
    )

    return redirect("/")

def display_book(request, book_id):
    context = {
        "book": Book.objects.get(id = book_id),
        "authors": Author.objects.all()
    }

    return render(request,"book.html", context)

def add_author(request,book_id):
    this_book = Book.objects.get(id = book_id)
    this_author = Author.objects.get(id = request.POST['author_id'])

    this_book.authors.add(this_author)
    return redirect(f"/books/{book_id}")

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }

    return render(request,"index2.html", context)

def create_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )

    return redirect("/authors")

def display_author(request, author_id):
    context = {
        "author": Author.objects.get(id = author_id),
        "books": Book.objects.all()
    }

    return render(request,"book2.html", context)

def add_book(request,author_id):
    this_author = Author.objects.get(id = author_id)
    this_book = Book.objects.get(id = request.POST['book_id'])

    this_author.books.add(this_book)
    return redirect(f"/authors/{author_id}")