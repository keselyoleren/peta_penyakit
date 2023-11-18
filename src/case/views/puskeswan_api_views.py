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