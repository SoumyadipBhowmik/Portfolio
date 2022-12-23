from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Home")

# Create your views here.
