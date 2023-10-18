from django.urls import path
from . import views
urlpatterns=[
    path('i/',views.index),
    path('ii/<classe>',views.index)
    
]