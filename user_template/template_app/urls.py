from django.urls import path, include
from . import views

urlpatterns = [
    path('', (views.index)),
    path('add_user',views.add_user)
]