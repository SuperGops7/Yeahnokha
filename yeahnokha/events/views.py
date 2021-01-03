from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def events_view(request):
    return HttpResponse("events page")