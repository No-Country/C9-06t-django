from django.shortcuts import render, redirect


def contact(request):
    context = {}

    return render(request, 'contact/contacto.html', context)


