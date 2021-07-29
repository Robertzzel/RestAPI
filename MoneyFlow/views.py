from rest_framework import generics, status
from .serializers import ProdusSerializer
from .models import Produs
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProduseView(generics.ListAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class AdaugaProdusView(APIView):

    def post(self, req):
        nume = req.data['nume']
        pret = float(req.data['pret'])
        data = req.data['data']

        new_obj = Produs(nume=nume, pret=pret, data=data)
        new_obj.save()

        return Response(req.data,status=status.HTTP_200_OK)