from django.urls import path
from . import views
from .views import Affiche,Supprimer,Detail,Ajout,Update
urlpatterns=[
    path('i/',views.index),
    path('ii/<classe>',views.index),
    # path('Affiche/',views.AfficheProjet),
    path('Liste/',Affiche.as_view(),name="Aff"),
    path('Delete/<int:pk>',Supprimer.as_view(),name='DD'),
    path('Detail/<int:pk>',Detail.as_view(),name='Detail'),
    path('Ajout/',Ajout.as_view(),name='aj'),
    path('Update/<int:pk>',Update.as_view(),name='Update')

    
]