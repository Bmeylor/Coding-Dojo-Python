from django.urls import path
from . import views

urlpatterns = [
    path('',(views.index)),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.display_book),
    path('books/<int:book_id>/add_author',views.add_author),
    path('authors',(views.authors)),
    path('authors/create', views.create_author),
    path('authors/<int:author_id>', views.display_author),
    path('authors/<int:author_id>/add_book',views.add_book),
]