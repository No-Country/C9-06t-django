from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

## Listado de criptos ##
# def users(request):
#     response = requests.get('http://api.coinlayer.com/list?access_key=787d56808e80ae8ccdc4e01e00a2818e')
    
#     if response.status_code == 200:
#         response_json= response.json()
#         origi = response_json['crypto']
#         lista = origi.values()
      
          
#     return render(request, 'badge/badge.html', {'lista':lista})    
 
## Tasa de las mismas ##
def users(request):
    response = requests.get('http://api.coinlayer.com/live?access_key=787d56808e80ae8ccdc4e01e00a2818e')
    
    if response.status_code == 200:
        response_json= response.json()
        origi = response_json['rates']
        tasa = origi.values()
        moneda = origi.keys()

          
    return render(request, 'badge/badge.html', {'tasa':tasa,'moneda':moneda})     
