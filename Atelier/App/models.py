from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
# from django.utils.timezone import datetime

def is_esprit_mail(value):
    if not str(value).endswith('@esprit.tn'):
        # return "Vote email n'est valide"+value
        raise ValidationError("Vote email n'est valide",
                              params={'value':value})
# Create your models here.
class User(models.Model):
    nom=models.CharField('Nom',max_length=30)
    prenom=models.CharField(max_length=30)
    email=models.EmailField(validators=[is_esprit_mail])
    def __str__(self):
        return 'le nom est '+self.nom+' le prenom est '+self.prenom
class Etudiant(User):
    groupe=models.CharField(max_length=30)
class Coach(User):
    pass
class Projet(models.Model):
    nom_projet=models.CharField('Titre Projet',max_length=30)
    duree_projet=models.IntegerField(default=0)
    temps_alloue_par_projet=models.IntegerField(
        'Temps Alloue',
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])
    besoin=models.CharField(max_length=30)
    description=models.TextField(max_length=100)
    est_valide=models.BooleanField(default=False)
    createur=models.OneToOneField(
        Etudiant,
        on_delete=models.CASCADE,
        related_name='project_owner' 
    )
    superviseur=models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        null=True,
        related_name='coach_name'
    )
    members=models.ManyToManyField(
        Etudiant,
        through='MemberShipInProject'
        
    )
    # creation_date=models.DateTimeField()
    class Meta:
        # verbose_name=('Project')
        verbose_name_plural=('Project')
        # models.CheckConstraint(
        #     check=models.Q(creation_date__gt=datetime.now(),
        #     name="Please Check the date!"))
        # Views.py
        # Projet.object.get(Q(creation_date__gt=datetime.now(),
        #                
    
class MemberShipInProject(models.Model):
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    tim_allocated_by_member=models.IntegerField(
             'Temps alloué par les membres')
    # class Meta:
    #     unique_together=('projet','etudiant')

