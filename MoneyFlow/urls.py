from django.urls import path
from .views import ProduseView,AdaugaProdusView

urlpatterns=[
    path('produse/',ProduseView.as_view()),
    path('adauga-produs/',AdaugaProdusView.as_view()),
]