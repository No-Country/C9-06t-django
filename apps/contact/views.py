from django.shortcuts import render, redirect

def contacto(request):
    context = {}

    return render(request, 'contact/contacto.html', context)


