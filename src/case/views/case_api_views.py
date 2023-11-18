from time import time
from rest_framework import (
    generics,
    status,
    viewsets,
    response
)

from django.utils import timezone

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
        
    def get_queryset(self):
        time_filter = self.request.query_params.get('time_filter', 'all')
        if time_filter:
            if time_filter == 'today':
                start_date = timezone.now().date()
                end_date = start_date + timezone.timedelta(days=1)
            elif time_filter == 'this_week':
                end_date = timezone.now().date()
                start_date = end_date - timezone.timedelta(days=7)
            elif time_filter == 'this_month':
                end_date = timezone.now().date()
                start_date = end_date - timezone.timedelta(days=30)
            elif time_filter == 'this_year':
                end_date = timezone.now().date()
                start_date = end_date - timezone.timedelta(days=365)
            else:
                return super().get_queryset()        
            return super().get_queryset().filter(created_at__range=[start_date, end_date])

        return super().get_queryset()        

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)