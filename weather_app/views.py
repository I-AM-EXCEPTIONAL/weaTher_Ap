from django.shortcuts import render
import requests
import os

def get_weather_data(latitude, longitude):
    key = '83c2e6b3b8f34b5eb770212d2d3cde6f'
    url = f'https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={key}'

    try:
        result = requests.get(url).json()
        return result['data'][0]['temp']
    except requests.exceptions.RequestException as e:
        print(f'Error making API request: {e}')
        return None
    except KeyError:
        print('Error parsing API response')
        return None

def home(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Validate latitude and longitude (add your validation logic here)

        temp = get_weather_data(latitude, longitude)

        context = {
            'latitude': latitude,
            'longitude': longitude,
            'temp': temp,
        }
    else:
        context = {}

    return render(request, 'index.html', context)
