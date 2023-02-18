from django.urls import path
from apps.base.views import * 

urlpatterns = [
    path('', home, name="home"),
    path('servicios/', sercicios, name="servicios"),
    path('soporte/', soporte, name="soporte"),
    path('empresa/', empresa, name="empresa"),

]
