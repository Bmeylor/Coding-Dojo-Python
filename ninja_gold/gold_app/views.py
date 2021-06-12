from django.shortcuts import render, redirect
import random
from time import gmtime,strftime

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render (request,"index.html")

def process(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if request.POST['location'] == "farm":
        add_gold = random.randint(10,20)
        activity = f"Earned {add_gold} from Farm at {time}"

    elif request.POST['location'] == "cave":
        add_gold = random.randint(5,10)
        activity = f"Earned {add_gold} from Cave at {time}"

    elif request.POST['location'] == "house":
        add_gold = random.randint(2,5)
        activity = f"Earned {add_gold} from House at {time}"

    elif request.POST['location'] == "casino":
        add_gold = random.randint(-50,50)
        if add_gold < 0:
            activity = f"Lost {add_gold} from Casino at {time}"
        else:
            activity = f"Earned {add_gold} from Casino at {time}"

    request.session['gold'] += add_gold
    request.session['activities'].append(activity)
    
    return redirect("/")