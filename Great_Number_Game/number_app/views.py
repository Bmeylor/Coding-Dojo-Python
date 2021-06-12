from django.shortcuts import render, redirect
import random


# Create your views here.

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1,100)
    if 'result' not in request.session:
        request.session['result'] = ""
    print(request.session['number'])
    print(request.session['result'])
    return render(request, "index.html")

def guess(request):
    guess = int(request.POST['guess'])
    if guess == request.session['number']:
        print("Got the Number")
        request.session['result'] = "Got the Number"
    elif guess < request.session['number']:
        print("Too Low")
        request.session['result'] = "Too Low"
    else:
        print("Too High")
        request.session['result'] = "Too High"
    return redirect('/')
    

