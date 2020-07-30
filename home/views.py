from django.shortcuts import render
import requests

def coronaData():
    response = requests.get("https://corona-api.com/timeline")
    return response.json()['data'][0]

def coronaDataName(id):
    response = requests.get("https://corona-api.com/countries/"+id)
    return response.json()
        
def countriesData():
    response = requests.get("http://restcountries.eu/rest/v2/all")
    return response.json()

def cekURLAPI(id):
    response = requests.get("https://corona-api.com/countries/"+id).status_code
    return response

def index(request):
    context = {
        'data' : [
                    ['/', 'Home', 'icon-home'],
                    ['country/', 'Country', 'icon-flag'],
                    ['about/', 'About', 'icon-human'],
                 ],
        'carousel' : [
            {
                'id' : 1,
                'title': 'confirmed',
                'icon' : 'icon-virus',
                'color' : 'blue-filter'
            },
            {
                'id' : 2,
                'title': 'deaths',
                'icon' : 'icon-death',
                'color' : 'red-filter'
            },
            {
                'id' : 3,
                'title': 'recovered',
                'icon' : 'icon-recovery',
                'color' : 'green-filter'
            }
        ],
        'coronaData' : coronaData(),
        'dataGlobal' : True,
        'countriesData' : countriesData()
    }
    
    return render(request, 'Home/index.html', context)

def country(request):
    context = {
        'data' : [
                    ['/', 'Home', 'icon-home'],
                    ['/country', 'Country', 'icon-flag'],
                    ['/about', 'About', 'icon-human'],
                 ],
        'countriesData': countriesData()
    }

    return render(request, 'countries/index.html', context)

def countryHome(request, *, country_requested):
    dataEmpty = False
    if cekURLAPI(f'{country_requested}') == 200:
        dataEmpty = False
    else:
        dataEmpty = True
    context = {
        'data' : [
                    ['/', 'Home', 'icon-home'],
                    ['/country/', 'Country', 'icon-flag'],
                    ['/about/', 'About', 'icon-human'],
                ],
        'carousel' : [
            {
                'id' : 1,
                'title': 'confirmed',
                'icon' : 'icon-virus',
                'color' : 'blue-filter'
            },
            {
                'id' : 2,
                'title': 'deaths',
                'icon' : 'icon-death',
                'color' : 'red-filter'
            },
            {
                'id' : 3,
                'title': 'recovered',
                'icon' : 'icon-recovery',
                'color' : 'green-filter'
            }
        ],
        'coronaData': coronaDataName(f'{country_requested}'),
        'dataGlobal' : False,
        'dataEmpty' : dataEmpty,
        'countriesData' : countriesData()
    }
        # data = requests.get(f'https://corona-api.com/countries/{country_requested}').json()
    
    return render(request, 'Home/index.html', context)
        