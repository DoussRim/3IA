from django.shortcuts import render
from django.http import HttpResponse
from App.models import Projet
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import ProjetAdd
# Create your views here.
def index(request,classe):
    # return HttpResponse('Bonjour <i>3IA</i>')
    # return HttpResponse('Bonjour '+classe)
    return render(request,'App/index.html',
                  {'c':classe})
# def Affiche(request):
#     etudiant=Etudiant.objects.order_by(-"username");
# def AfficheProjet(request):
#     projets=Projet.objects.all()#select * from projet
#     # resultat='-'.join(p.nom_projet for p in projet)
#     # return HttpResponse(resultat)
#     return render(request,'App/Affiche.html',
#                   {'p':projets})
class Affiche(ListView):
    model=Projet
    context_object_name="p"
    # template_name="App/Affiche.html"
    ordering=['-nom_projet']
    # fields="__all__"
class Supprimer(DeleteView):
    model=Projet
    success_url=reverse_lazy('Aff')
class Detail(DetailView):
    model=Projet
    template_name="App/Detail.html"
class Ajout(CreateView):
    model=Projet
    # fields="__all__"
    form_class=ProjetAdd
    success_url=reverse_lazy('Aff')
class Update(UpdateView):
    model=Projet
    form_class=ProjetAdd
    template_name="App/Update.html"