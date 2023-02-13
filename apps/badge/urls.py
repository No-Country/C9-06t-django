from django.urls import path
from . import views

urlpatterns = [
    path('badge/', views.badge, name="badge"),
]
