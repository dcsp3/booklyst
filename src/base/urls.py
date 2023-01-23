from django.urls import path
from . import views

urlpatterns = [
    path('', views.readbooks, name="read"),
    path('read-later/', views.unreadbooks, name="unread"),
    path('add/', views.addBook, name="add-book"),
    path('edit/<str:book_id>/', views.editBook, name="edit-book"),
    path('delete/<str:book_id>/', views.deleteBook, name="delete-book"),
    path('<str:book_id>/', views.read_book, name="read-book"), 
    path('read-later/add/', views.addUnreadBook, name="add-unread-book"),
    path('read-later/delete/<str:book_id>/', views.deleteUnreadBook, name="delete-unread-book"), 
]
