from django.shortcuts import render
from .models import Projeto


def home(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'pascucci/home.html', context)