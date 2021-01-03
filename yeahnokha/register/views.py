from django.shortcuts import render
from django.http import HttpResponse

from .models import Register

# Create your views here.

def register_view(request):
    return render(request, "register.html")

def register_success_view(request):
    part_name = request.POST["part_name"]
    part_inst = request.POST["part_inst"]
    part_email = request.POST["part_email"]
    part_phone = request.POST["part_phone"]

    register_info = Register(part_name=part_name, part_inst=part_inst, part_email=part_email, part_phone=part_phone)
    register_info.save()

    return HttpResponse("Registeration Successful!")