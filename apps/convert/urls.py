from django.urls import path
from apps.convert.views import *

urlpatterns = [
    path('convert/', requirement, name="converter"),
]
