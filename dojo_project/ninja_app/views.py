from django.shortcuts import render,redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context ={
        'total_dojos': Dojo.objects.all(),
        'total_ninjas': Ninja.objects.all()
    }
    return render(request,"index.html",context)


def add_dojo(request):
    Dojo.objects.create(
        name=request.POST['add_name'],
        city=request.POST['add_city'],
        state=request.POST['add_state']
    )
    return redirect('/')


def add_ninja(request):
    my_dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        school=my_dojo
    )
    return redirect('/')