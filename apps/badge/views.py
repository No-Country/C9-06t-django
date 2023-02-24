from django.shortcuts import render, redirect
from django.http import HttpResponse
import aiohttp
import asyncio

async def list(request):
    async with aiohttp.ClientSession() as session2:
       async with session2.get('http://api.coinlayer.com/list?access_key=ab2978034ee6b835f2e20c4c75a4f51b', ) as respo2:
                    if respo2.status  == 200:
                        data2 = await respo2.json()
                        b = data2['crypto']  
                    return render(request, 'badge/list.html',{'list':b  }) 
                             

async def expand(request):
    async with aiohttp.ClientSession() as session3:
        async with session3.get('http://api.coinlayer.com/live?access_key=ab2978034ee6b835f2e20c4c75a4f51b&expand=1', ) as resp3:
                    if resp3.status  == 200:
                        data3 = await resp3.json()
                        c = data3['rates']
                    return render(request, 'badge/expand.html',{'expand':c } )  
                

