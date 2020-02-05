from bondportfolio.models import Bond
from bondportfolio.serializers import BondSerializer
from rest_framework import generics

class BondListCreate(generics.ListCreateAPIView):
    queryset = Bond.objects.all()[0:10]
    serializer_class = BondSerializer

class BondFilter(generics.ListAPIView):
    serializer_class = BondSerializer

    def get_queryset(self):
        minTenor = self.request.query_params.get('minTenor', '0')
        maxTenor = self.request.query_params.get('maxTenor', '1000')
        minYTM = self.request.query_params.get('minYTM', '0')
        print(self.request.query_params)
        queryset = Bond.objects.filter(tenor__gte=minTenor).filter(tenor__lte=maxTenor).filter(ytm__gte=minYTM).order_by('-ytm')
        print(list(queryset))
        return queryset

class BondSelector(generics.ListAPIView):
    serializer_class = BondSerializer

    def get_queryset(self):
        minTenor = self.request.query_params.get('minTenor', '0')
        maxTenor = self.request.query_params.get('maxTenor', '1000')
        minYTM = self.request.query_params.get('minYTM', '0')

        queryset = Bond.objects.filter(tenor__gte=minTenor).filter(tenor__lte=maxTenor).filter(ytm__gte=minYTM).order_by('-ytm')
        print(queryset)
        return queryset