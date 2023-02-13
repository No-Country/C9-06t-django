from django.shortcuts import render, redirect

def badge(request):
    context = {}

    return render(request, 'badge/badge.html', context)

