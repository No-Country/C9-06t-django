from django.shortcuts import render, redirect
from django.views.generic import CreateView
from apps.contact.models import ContactModel


class ContacCreateView (CreateView):
    model = ContactModel
    template_name = 'contact/contacto.html'
    fields = ('__all__')
    success_url = '/'
