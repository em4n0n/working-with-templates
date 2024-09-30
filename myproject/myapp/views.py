from django.shortcuts import render

# Create your views here.

def home(request):
    render(request, "home.html")
    
def menu(request):
    render(request, "menu.html")
    