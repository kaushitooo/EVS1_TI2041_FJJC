from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista2(request):
    html= """
    <h2>Proyecto rama 2</h2>
    <p Style="color:blue">Lorem ipsum es el texto que se usa habitualmente en diseño gráfico en <b>demostraciones de tipografías o de borradores</b> <br>de diseño para probar el diseño visual antes de insertar el texto final.</p>
"""
    return HttpResponse(html)