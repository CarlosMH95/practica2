from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def get_time(request,horas_adicionales):
    ahora=datetime.datetime.now() +datetime.timedelta(hours=int(horas_adicionales))
    html= '<html><head><body>%s</body></head></html>'% ahora
    return HttpResponse(html)
    
def get_saludo(request,nombre):
    html='<html><head><body> Hola %s</body></head></html>'% nombre
    return HttpResponse(html)