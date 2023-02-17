import aiohttp
from django.shortcuts import render

# Create your views here.

async def example(request):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://api.coinlayer.com/live") as res:
            data = await res.json()
            print(data)
    return render(
        request,
        "index.html",
        {"data": data}
    )