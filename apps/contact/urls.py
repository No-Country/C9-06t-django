from django.urls import path
from . import views

urlpatterns = [
    path(
        'contact/',
        views.ContacCreateView.as_view(),
        name="contacto"
    ),
]
