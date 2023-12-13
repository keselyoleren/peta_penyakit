from rest_framework import (
    generics,
    viewsets,
    response
)

from case.models import *
from case.serialize.address_serialize import *
from case.serialize.feedback_serialize import FeedbackSerialize, RetrevieFeedbackSerialize
from config.pagination import ResponsePagination

from rest_framework.permissions import AllowAny, IsAuthenticated
from manage_users.models import AccountUser, Feedback


class FeedbackApiView(viewsets.ModelViewSet):
    serializer_class = FeedbackSerialize
    queryset = Feedback.objects.all()
    permission_classes = [AllowAny | IsAuthenticated]
    pagination_class = ResponsePagination
    
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            puskeswan = Puskeswan.objects.filter(id=self.request.user.puskeswan.id).first()
            user = AccountUser.objects.filter(puskeswan=puskeswan)
            return super().get_queryset().filter(sub_district__in=puskeswan.wilayah_pelayanan.all())
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RetrevieFeedbackSerialize
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        validate_data = request.data
        if self.request.user.is_authenticated:
            validate_data['created_by'] = request.user.id
        serialize = self.serializer_class(data=validate_data)
        serialize.is_valid(raise_exception=True)
        self.perform_create(serialize)
        serialize_data = RetrevieFeedbackSerialize(serialize.instance)
        return response.Response(serialize_data.data)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)