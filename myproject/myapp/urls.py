from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('book/', views.book),
    path('home/', views.home),
    path('menu/', views.menu),
]
