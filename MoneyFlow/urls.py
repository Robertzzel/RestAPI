from django.urls import path
from .views import *

urlpatterns=[
    path('produse/',ProduseView.as_view()),
    path('adauga-produs/',AdaugaProdusView.as_view()),
    path('produse-ultima_saptamana/', UltimaSaptamanaView.as_view()),
    path('produse-ultima_luna/', UltimaLunaView.as_view()),
]