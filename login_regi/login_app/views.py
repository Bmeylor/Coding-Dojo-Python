from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)    
        
        return redirect('/')
    
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name= request.POST['first_name'],
            last_name =request.POST['last_name'],
            email = request.POST['email'],
            password= pw_hash,
            )
        
        return redirect("/success")
        
    
def login(request):

    try:
        user = User.objects.get(email = request.POST['email'])
    except:
            messages.error(request,"Incorrect Email or Password")
            return redirect('/')

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            request.session['user_first_name'] = user.first_name
            request.session['user_last_name'] =user.last_name
            request.session['user_email'] = user.email
            return redirect("/success")

    messages.error(request,"incorrect email or password")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request,"Please log in")
        return redirect('/')
    return render(request,'index2.html')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_first_name' in request.session:
        del request.session['user_first_name']
    if 'user_last_name' in request.session:
        del request.session['user_last_name']
    if 'user_email' in request.session:
        del request.session['user_email']
    return redirect('/')