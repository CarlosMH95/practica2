from Persona import views
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns=[
    url(r'^tiempo/(?P<horas_adicionales>\d+)/', views.get_time),
    url(r'^saludo/(?P<nombre>[A-Z]+)/', views.get_saludo),
    url(r'(?P<nombre>[A-Z]+)/(?P<horas_adicionales>\d+)/', views.get_saludo_hora),
]