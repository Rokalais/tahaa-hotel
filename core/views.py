from django.shortcuts import render

# Vistas de la aplicación principal

def Home(request):
    return render(request,"core/home.html")

def AboutUs(request):
    return render(request,"core/about.html")

