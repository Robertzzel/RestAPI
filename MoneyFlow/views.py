from rest_framework import generics, status
from .serializers import ProdusSerializer
from .models import Produs
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

# Create your views here.

class ProduseView(generics.ListAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class AdaugaProdusView(APIView):
    def post(self, req):
        nume: str = req.data['nume']
        pret: float = float(req.data['pret'])
        data = req.data['data']

        #procesam data sa fie datetime
        data = data.split('-')
        if len(data[1]) == 1: data[1] = f"0{data[1]}" #facem luna "0X" in caz ca e "X"
        data = datetime.date(int(data[0]), int(data[1]), int(data[2]))

        new_obj = Produs(nume=nume, pret=pret, data=data)
        new_obj.save()

        return Response(req.data,status=status.HTTP_200_OK)


class SaptamanalView(generics.ListAPIView):
    azi = datetime.date.today()
    luniaAceasta = azi - datetime.timedelta(days= azi.weekday())
    queryset = Produs.objects.filter(data__gte=luniaAceasta)
    serializer_class = ProdusSerializer

class LunarView(generics.ListAPIView):
    azi = datetime.date.today()
    primaZiDinLuna = azi - datetime.timedelta(days= azi.day-1)
    queryset = Produs.objects.filter(data__gte=primaZiDinLuna)
    serializer_class = ProdusSerializer
