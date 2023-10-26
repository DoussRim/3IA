
from django import forms
from .models import Projet
from django.forms import Textarea
class ProjetAdd(forms.ModelForm):
    class Meta:
        model=Projet
        fields=('__all__')
        # fields=('nom_projet','besoin')
        widgets={'besoin':Textarea(
            attrs={'cols':20,'rows':20}
        )}
        
    