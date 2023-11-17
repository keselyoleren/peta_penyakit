from rest_framework import (
    generics,
    status,
    viewsets,
    response
)

from case.models import *
from case.serialize.address_serialize import *
from config.pagination import ResponsePagination


class ProvicnceViews(generics.ListAPIView):
    serializer_class = ProvinceSerialize
    queryset = Province.objects.all()
    pagination_class = ResponsePagination
    
    def list(self, request, *args, **kwargs):
        instance = self.queryset.all()
        page = self.paginate_queryset(instance)
        serializer = self.get_paginated_response(
            self.serializer_class(page, many=True).data
        )
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class RegencyApiView(generics.ListAPIView):
    serializer_class = RegencySerialize
    queryset = Regency.objects.all()
    pagination_class = ResponsePagination
    
    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter(province=kwargs['province_id'])
        page = self.paginate_queryset(instance)
        serializer = self.get_paginated_response(
            self.serializer_class(page, many=True).data
        )
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class SubDistrictApiView(generics.ListAPIView):
    serializer_class = SubDistrictSerialize
    queryset = SubDistrict.objects.all()
    pagination_class = ResponsePagination
    
    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter(regency=kwargs['regency_id'])
        page = self.paginate_queryset(instance)
        serializer = self.get_paginated_response(
            self.serializer_class(page, many=True).data
        )
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class VillageApiView(generics.ListAPIView):
    serializer_class = VillageSerialize
    queryset = Village.objects.all()
    pagination_class = ResponsePagination
    
    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter(sub_district=kwargs['sub_district_id'])
        page = self.paginate_queryset(instance)
        serializer = self.get_paginated_response(
            self.serializer_class(page, many=True).data
        )
        return response.Response(serializer.data, status=status.HTTP_200_OK)