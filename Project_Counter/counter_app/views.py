from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_visits':num_visits,
    }
    return render(request,'index.html', context )

def destroy_session(request):
    del request.session['num_visits']
    return redirect("/")