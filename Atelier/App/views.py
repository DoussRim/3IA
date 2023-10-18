from django.shortcuts import render
from django.http import HttpResponse
from App.models import Etudiant
# Create your views here.
def index(request,classe):
    # return HttpResponse('Bonjour <i>3IA</i>')
    # return HttpResponse('Bonjour '+classe)
    return render(request,'App/index.html',
                  {'c':classe})
def Affiche(request):
    etudiant=Etudiant.objects.order_by(-"username");