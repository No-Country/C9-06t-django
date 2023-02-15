import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from exmoney.settings import API_KEY

COINLAYER_API = "http://api.coinlayer.com/api/list" + API_KEY


def requirement(request):
    resp = requests.get(COINLAYER_API)

    if resp.status_code != 200:
        return HttpResponse('ERROR GET ' + COINLAYER_API + ' {}'.format(resp.status_code))
    users = resp.json()
    print(users)
    # return JsonResponse(resp.json())
    return render(request, 'convert/convert.html', {"users": users})


# def requirement(request):
#     resp = requests.get(COINLAYER_API)

#     if resp.status_code != 200:
#         return HttpResponse('ERROR GET ' + COINLAYER_API + ' {}'.format(resp.status_code))
#     jres = JsonResponse(resp.json())
#     context = {"form":jres}
#     print(jres)
#     # return JsonResponse(resp.json())
#     return render(request, 'convert/convert.html', context)

# def moneyList(request):
#     form = getList()
#     list = form.objects.all()
#     context = {"form":list}
#     return render(request, 'convert/convert.html', context)


