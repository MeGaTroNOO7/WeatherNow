from django.shortcuts import render

def index(request):
    return render(request, 'weathernow/index.html') #returns the index.html template