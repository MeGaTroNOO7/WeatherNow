from django.shortcuts import render

def index(request):
    return render(request, 'templates/weathernow/index.html') #returns the index.html template