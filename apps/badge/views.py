from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def users(request):
    context = {}

    return render(request, 'badge/badge.html', context)





# def users(request):
#     liv_response = requests.get('http://api.coinlayer.com/live?access_key=787d56808e80ae8ccdc4e01e00a2818e')
#     list_response = requests.get('http://api.coinlayer.com/list?access_key=787d56808e80ae8ccdc4e01e00a2818e')
    
#     if liv_response.status_code and list_response.status_code ==  200:

#         liv_json = liv_response.json ()
#         rates = liv_json['rates']
#         tasa = rates.values()
#         moneda = rates.keys()

#         list_json = list_response.json ()
#         crypto = list_json['crypto']
#         crypto_values  = crypto.values()
    
          
#     return render(request, 'badge/badge.html',{'tasa':tasa, 'moneda':moneda,'crypto':crypto_values} )     
 
