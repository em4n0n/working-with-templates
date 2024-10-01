from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name= "about"),
    path('book/', views.book, name = "book"),
    path('home/', views.home, name = "home"),
    path('menu/', views.menu, name = "menu"),
]
