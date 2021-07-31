from rest_framework import generics, status
from .serializers import ProdusSerializer
from .models import Produs
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime


class ProduseView(generics.ListAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class AdaugaProdusView(APIView):
    def post(self, req):
        nume: str = req.data['nume'].capitalize()
        pret: float = float(req.data['pret'])
        data = req.data['data']

        #procesam data sa fie datetime
        data = data.split('-')
        if len(data[1]) == 1: data[1] = f"0{data[1]}" #facem luna "0X" in caz ca e "X"
        data = datetime.date(int(data[0]), int(data[1]), int(data[2]))

        new_obj = Produs(nume=nume, pret=pret, data=data)
        new_obj.save()

        return Response(req.data,status=status.HTTP_200_OK)


class UltimaLunaView(APIView):
    def get(self, req):
        azi = datetime.date.today()
        primaZiDinLuna = azi - datetime.timedelta(days= azi.day-1)
        query = Produs.objects.filter(data__gte=primaZiDinLuna)
        raspuns=adunaProduseRepetate(query)

        return Response(raspuns ,status=status.HTTP_200_OK)


class UltimaSaptamanaView(APIView):
    def get(self, req):
        azi = datetime.date.today()
        luniaAceasta = azi - datetime.timedelta(days= azi.weekday())
        query = Produs.objects.filter(data__gte=luniaAceasta)
        raspuns=adunaProduseRepetate(query)

        return Response(raspuns ,status=status.HTTP_200_OK)


class AnumitaLunaView(APIView):
    def get(self,req,luna):
        raspuns = []
        primaZiDinLuna: datetime.date
        ultimaZiDinLuna: datetime.date
        primaZiDinLunaActuala = datetime.date.today().replace(day=1)

        primaZiDinLuna = primaZiDinLunaActuala.replace(month=primaZiDinLunaActuala.month-luna)
        ultimaZiDinLuna = primaZiDinLuna.replace(month=primaZiDinLuna.month+1) - datetime.timedelta(days=1)

        print(primaZiDinLuna,ultimaZiDinLuna)

        query = Produs.objects.filter(data__gte=primaZiDinLuna,data__lte=ultimaZiDinLuna)
        queryProcesat = adunaProduseRepetate(query)

        return Response(queryProcesat,status=status.HTTP_200_OK)


# returneaza doar numele si pretul , nu si data
def adunaProduseRepetate(query):
    resp: dict = {}
    raspuns = []
    for record in query:
        if record in resp:
            resp[record.nume] += record.pret
        else:
            resp[record.nume] = record.pret

    #pana aici raspunsul e de tip {produs1:pret1,produs2:pret2, ...}
    #dar mie imi tb [{nume:"produs1",pret:"pret1"}, ...]

    for k,v in resp.items():
        raspuns.append({
            "nume": k,
            "pret": v,
        })

    return raspuns