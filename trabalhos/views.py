from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Projetos

# Create your views here.


def home(request):
    projetos = Projetos.objects.all()
    return render(request,'base.html',{'projetos':projetos})



def details(request,id):
    projeto = get_object_or_404(Projetos,pk=id)
    return render(request,'detalhe.html',{'projeto':projeto})