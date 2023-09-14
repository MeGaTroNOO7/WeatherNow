from django.shortcuts import render
import requests
from urllib.parse import quote
from .models import City
from .forms import CityForm

def index(request):
    weather_data = []  # Define weather_data outside of the if block

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            try:
                api_key = 'a6e4d71ca1f45ad86b009d61f58526f9'  # Your API key
                city_name_encoded = quote(city_name)
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name_encoded}&units=imperial&appid={api_key}'
                city_weather = requests.get(url).json()
                
                if 'main' in city_weather and 'temp' in city_weather['main'] and 'weather' in city_weather:
                    weather = {
                        'city': city_name,
                        'temperature': city_weather['main']['temp'],
                        'description': city_weather['weather'][0]['description'],
                        'icon': city_weather['weather'][0]['icon'],
                        'humidity': city_weather['main']['humidity'],
                        'pressure': city_weather['main']['pressure'],
                        'country': city_weather['sys']['country'],
                        'sunrise': city_weather['sys']['sunrise'],
                        'sunset': city_weather['sys']['sunset'],
                        'windspeed': city_weather['wind']['speed']
                    }
                    weather_data = [weather]
                else:
                    print(f"API response for {city_name} does not have the expected structure.")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data for {city_name}: {e}")
        else:
            print("Form is not valid")
    else:
        form = CityForm()

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)
