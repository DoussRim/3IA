from django.contrib import admin,messages
from .models import *
# Register your models here.
class MemberProject(admin.StackedInline):
    model=MemberShipInProject
    extra=1
class SearchEtudiant(admin.ModelAdmin):
    search_fields=['nom']
class ProjetAdmin(admin.ModelAdmin):
    list_display=('nom_projet','duree_projet',
                  'temps_alloue_par_projet',
                  'est_valide','createur')
    def set_to_valid(self,request,queryset):
        queryset.update(est_valide=True)
    set_to_valid.short_description='Validate'
    def set_to_no_valid(self,request,queryset):
        row=queryset.filter(est_valide=False)
        if(row.count()>0):
            messages.error(request,
                "%s this article are already invalid"
                %row.count())
        else:
            a=queryset.update(est_valide=False)
            messages.success(request,
                "%s projects was updated"%a)
    set_to_no_valid.short_description='No Validate'
    actions=['set_to_valid','set_to_no_valid']
    inlines=(MemberProject,)
    fieldsets=(
        ('A propos',{'fields':('nom_projet',
                    'besoin','description')}),
        ('Etat',{'fields':('est_valide',)}),
        ('Durée',{'fields':('duree_projet',
                            'temps_alloue_par_projet')}),
        (None,{'fields':('createur','superviseur')})
    )
    autocomplete_fields=['createur']
    list_filter=('est_valide','createur')
    search_fields=['nom_projet']
    actions_on_bottom=True
    actions_on_top=False

admin.site.register(Projet,ProjetAdmin)
admin.site.register(Coach)
admin.site.register(Etudiant,SearchEtudiant)