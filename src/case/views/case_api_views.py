from rest_framework import (
    generics,
    status,
    viewsets,
    response
)

from case.models import *
from case.serialize.address_serialize import *
from case.serialize.case_serializer import CaseSerialize
from case.serialize.diseases_serialize import DiseasesSerialize
from config.pagination import ResponsePagination

from rest_framework.permissions import AllowAny, IsAuthenticated


class CaseApiView(generics.ListAPIView):
    serializer_class = CaseSerialize
    queryset = Case.objects.all()
    permission_classes = [AllowAny | IsAuthenticated]
    pagination_class = ResponsePagination
        
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)