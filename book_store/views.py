from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return HttpResponse("This project working")