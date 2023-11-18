from rest_framework import (
    generics,
    status,
    viewsets,
    response
)

from case.models import *
from case.serialize.address_serialize import *
from config.pagination import ResponsePagination

from rest_framework.permissions import AllowAny, IsAuthenticated


class PueskeswanSubDistrictApiView(generics.ListAPIView):
    serializer_class = SubDistrictPuskeswanSerialize
    queryset = SubDistrict.objects.all()
    permission_classes = [AllowAny | IsAuthenticated]
    pagination_class = ResponsePagination
    
    def get_queryset(self):
        puskeswan = Puskeswan.objects.all()
        if self.request.user.is_authenticated:
            puskeswan = Puskeswan.objects.filter(id=self.request.user.puskeswan.id)
        wil_pelayanan_ids = []
        for x in puskeswan:
            wil_pelayanan_ids.extend([wil.id for wil in x.wilayah_pelayanan.all()])
        return super().get_queryset().filter(id__in=wil_pelayanan_ids)

    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PueskeswanSubDistrictVillageApiView(viewsets.ModelViewSet):
    serializer_class = SubDistrictAndVillagePuskeswanSerialize
    queryset = SubDistrict.objects.all()
    permission_classes = [AllowAny | IsAuthenticated]
    pagination_class = ResponsePagination
    
    def get_queryset(self):
        puskeswan = Puskeswan.objects.all()
        if self.request.user.is_authenticated:
            puskeswan = Puskeswan.objects.filter(id=self.request.user.puskeswan.id)
        wil_pelayanan_ids = []
        for x in puskeswan:
            wil_pelayanan_ids.extend([wil.id for wil in x.wilayah_pelayanan.all()])
        return super().get_queryset().filter(id__in=wil_pelayanan_ids)

    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = SubDistrict.objects.get(id=kwargs['sub_district_id'])
        except:
            return response.Response({'message': f"Subdistrict with id {kwargs['sub_district_id']} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)