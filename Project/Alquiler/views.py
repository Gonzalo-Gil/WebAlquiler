from django.shortcuts import render

def combos(request):
    return render(request, "combos.html", {})
