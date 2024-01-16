from django.shortcuts import render
from .models import Combo

def combos(request):
    combos = Combo.objects.all()
    return render(request, "combos.html", {'combos':combos})
