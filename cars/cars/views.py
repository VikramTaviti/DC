from django.urls import path
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("hey there! it's the homepage")