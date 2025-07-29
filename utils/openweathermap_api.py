import requests
from decouple import config

API_KEY = config('MINHA_API_KEY')

def buscar_cidade(CITY_NAME, API_KEY, STATE_CODE="", COUNTRY_CODE="", LIMIT=0):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={CITY_NAME},{STATE_CODE},{COUNTRY_CODE}&limit={LIMIT}&appid={API_KEY}")
    if response.status_code != 200:
        return None, None
    data = response.json()
    if not data:
        return None, None
    
    lat = data[0]['lat']
    lon = data[0]['lon']
    return lat, lon

def verificar_clima(lat, lon, API_KEY):
    reponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br")
    if reponse.status_code != 200:
        return None, None
    data = reponse.json()
    if not data:
        return None, None
    return data


buscar_cidade('Garopaba', API_KEY)