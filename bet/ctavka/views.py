from django.shortcuts import render
import requests
from .models import Ctavka

def index(request):

    Ctavkas = Ctavka.objects.all()

    context = {
        'Ctavkas': Ctavkas,
    }

    return render(request,'index.html',context)
