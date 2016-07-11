from django.shortcuts import render, redirect
from loja.models import Caneta
from django.views.generic import View

def index(request):
    return render(request, "index.html")

def canetas(request):
    todas_as_canetas = Caneta.objects.all()
    print(todas_as_canetas)
    return render(request, "canetas.html", {"canetas": todas_as_canetas});

class CadastrarCanetas(View):
    def get(self, request):
        return render(request, "cria_canetas.html")

    def post(self, request):
        caneta = Caneta()
        caneta.marca = request.POST['marca']
        caneta.cor = request.POST['cor']
        caneta.save()
        return redirect("/canetas")