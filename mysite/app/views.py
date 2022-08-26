from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la visa de encuestas! Falopa ñau")
    
def suma(request, n1, n2):
    return HttpResponse("La suma de "+str(n1)+" + "+str(n2)+" = "+ str(n1+n2))

def resta(request, n1, n2):
    return HttpResponse("La resta de "+str(n1)+" - "+str(n2)+" = "+ str(n1-n2))

def multiplicacion(request, n1, n2):
    return HttpResponse("La multiplicacion de "+str(n1)+" x "+str(n2)+" = "+ str(n1*n2))

# Create your views here.