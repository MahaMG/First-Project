from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def printHello(request):
    return HttpResponse("Hello World, This is my new HOME !")