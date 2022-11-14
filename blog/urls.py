# blog/urls.py
from django.urls import path
from .views import VistaPaginaInicio

urlpatterns = [
  path('', VistaPaginaInicio.as_view(), name='inicio'),
]