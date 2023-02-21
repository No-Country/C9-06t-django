from django.urls import path
from . import views


urlpatterns = [
    path('live/', views.live, name="live"),
    path('list/', views.list, name="list"),
    path('expand/', views.expand, name="expand"),
]
