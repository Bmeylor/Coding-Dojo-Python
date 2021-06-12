from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show


# Create your views here.
def index(request):

    return redirect('shows/')

def all_shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request,'all_shows.html',context,)

def new_show(request):
    return render(request, "new_show.html")

def create_show(request):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)    
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(
            title= request.POST['title'],
            network =request.POST['network'],
            release_date = request.POST['release_date'],
            description= request.POST['description']
        )
    return redirect(f"/shows/{new_show.id}")

def display_show(request, show_id):
    context = {
        "show": Show.objects.get(id = show_id)
    }
    return render(request,"one_show.html", context)

def edit_show(request,show_id):
    context = {
        "show": Show.objects.get(id= show_id)
    }
    return render(request,"update_show.html",context)

def update_show(request,show_id):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
            return redirect(f"/shows/{show_id}/edit")
    else:
        show = Show.objects.get(id = show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f"/shows/{show.id}")

def delete_show(request,show_id):
    show = Show.objects.get(id = show_id)
    show.delete()
    return redirect('/shows')


