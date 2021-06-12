from django.urls import path, include
from . import views

urlpatterns = [
    path('', (views.index)),
    path('add_dojo',(views.add_dojo)),
    path('add_ninja',(views.add_ninja)),
]