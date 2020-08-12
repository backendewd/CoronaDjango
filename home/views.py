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

def navData():
    data = [
                ['/', 'Home', 'icon-home'],
                ['country/', 'Country', 'icon-flag'],
                ['about/', 'About', 'icon-human']
            ]
    return data;

def gejala(request):
    context = {
        'data' : navData(),
        'gejala' : [
            {
                'id' : 1,
                'img': 'https://i.pinimg.com/originals/4f/03/17/4f0317d07429db450a618bd6778d9ce6.jpg',
                'title' : 'Sneezing',
            },
            {
                'id' : 2,
                'img': 'https://lh3.googleusercontent.com/proxy/4DOJk1-SZO1yIhTlfVkP8MVFyUldR9LziohsCSyuT5RptNW-il_D7XmKx8tPVZCTEiH1AiD7SUSTWidO4TjlmEyHierddgs1KCA=s0-d',
                'title' : 'fever',
            },
            {
                'id' : 3,
                'img': 'https://www.vippng.com/png/detail/3-34565_sleeping-emoji-png.png',
                'title' : 'Tired Easily',
            },
            {
                'id' : 4,
                'img': 'https://www.828ministries.com/populum/visuals/2019/09/2019-09-1-nauseated-face-facebook-865.png',
                'title' : 'Out Of Breath',
            }
        ],
        'coronaData' : coronaData(),
        'dataGlobal' : True,
        'countriesData' : countriesData()
    }
    return render(request, 'covid/gejala.html', context)

def index(request):
    context = {
        'data' : navData(),
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
        'data' : navData(),
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
        'data' : navData(),
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
        