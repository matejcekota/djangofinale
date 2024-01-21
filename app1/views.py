from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    aktualniHodina = datetime.now().hour
    if aktualniHodina < 10:
        pozdrav = "Dobré ráno"
    elif aktualniHodina < 18:
        pozdrav = "Dobrý den"
    else:
        pozdrav = "Dobrý večer"

    return render(request, 'main.html', {"pozdrav": pozdrav})

def form(request):
    return render(request, 'form.html')