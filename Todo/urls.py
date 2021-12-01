from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add_todo, name="add_todo"),
    path('update/<str:id>', views.update_todo, name="update_todo"),
    path('delete/<str:id>', views.delete_todo, name="delete_todo"),
    path('complete/<str:id>', views.complete_todo, name="complete_todo"),
]
