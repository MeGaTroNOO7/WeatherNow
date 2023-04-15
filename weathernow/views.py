from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a6e4d71ca1f45ad86b009d61f58526f9'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    return render(request, 'weather/index.html') #returns the index.html template