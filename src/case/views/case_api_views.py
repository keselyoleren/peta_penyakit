from datetime import datetime
from rest_framework import (
    generics,
    status,
    viewsets,
    response
)
from rest_framework import filters

from django.utils import timezone

from case.models import *
from case.serialize.address_serialize import *
from case.serialize.case_serializer import CaseSerialize
from case.serialize.diseases_serialize import DiseasesSerialize
from case.views.utils.imports import ImportProcess
from config.choice import ThreadResult
from config.pagination import ResponsePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated


class CaseApiView(generics.ListAPIView):
    serializer_class = CaseSerialize
    queryset = Case.objects.all()
    permission_classes = [AllowAny | IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    pagination_class = ResponsePagination
    search_fields = ['animal']
    filterset_fields = ['diseases']
    ordering_fields = ['id', 'created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_kecamatan = self.request.query_params.get('filter_kecamatan')
        time_filter = self.request.query_params.get('time_filter', 'all')

        if filter_kecamatan:
            queryset = queryset.filter(village__sub_district_id=filter_kecamatan)

        if time_filter in ['today', 'this_week', 'this_month', 'this_year']:
            end_date = timezone.now().date()
            if time_filter == 'today':
                start_date = end_date
            elif time_filter == 'this_week':
                start_date = end_date - timezone.timedelta(days=7)
            elif time_filter == 'this_month':
                start_date = end_date - timezone.timedelta(days=30)
            elif time_filter == 'this_year':
                start_date = end_date - timezone.timedelta(days=365)

            return queryset.filter(created_at__range=[start_date, end_date])

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ImportCaseView(generics.CreateAPIView):
    serializer_class = CaseSerialize
    queryset = Case.objects.all()
    permission_classes = [AllowAny | IsAuthenticated]

    def create(self, request, *args, **kwargs):
        result = ImportProcess().start_process(self.request.data)
        if result == ThreadResult.ALREADY_RUN:
            return response.Response({'message': 'Process import already in process'}, status=status.HTTP_208_ALREADY_REPORTED)
        elif result == ThreadResult.ERROR:
            return response.Response({'message': 'import Count error. Try again later'}, status=status.HTTP_400_BAD_REQUEST)
        elif result == ThreadResult.OK:
            return response.Response({'message': 'Process import started'}, status=status.HTTP_200_OK)
        return response.Response(status=status.HTTP_200_OK)
    
        