# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import City
from .forms import CityForm
from django.shortcuts import render
import requests

def climate(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d42e95b7dea8b06bfcaad713b41a2756'
    city='Delhi'

    if request.method == 'POST':
        form=CityForm(request.POST)
        form.save()
 
    form= CityForm()

    cities= City.objects.all()

    weather_data=[]

    for city in cities:
        response= requests.get(url.format(city)).json()
        weather={
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon']
                }
        weather_data.append(weather)
    weather_data=weather_data[::-1]        
    context={'weather_data': weather_data[0:3], 'form': form}
    return render(request,'weather/climate.html', context)
