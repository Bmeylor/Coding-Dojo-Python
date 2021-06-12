from django.shortcuts import render, redirect
from time import gmtime, strftime
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "time": datetime.now()
        
        #"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)


