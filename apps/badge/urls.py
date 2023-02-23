from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.list, name="list"),
    path('expand/', views.expand, name="expand"),
]
