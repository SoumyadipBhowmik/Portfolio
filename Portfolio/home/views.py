from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is my Portfolio")

# Create your views here.
