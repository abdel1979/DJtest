from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse(" Salam World - this is our first Django on Docker accesible from AWS ")
