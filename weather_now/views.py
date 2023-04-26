from django.shortcuts import render

def index(request):
    return render(request, 'weather_now/index.html') #returns the index.html template