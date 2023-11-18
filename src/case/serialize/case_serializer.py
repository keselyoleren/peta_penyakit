from rest_framework import serializers
from case.models import Case, Village
from case.serialize.address_serialize import VillageSerialize

class CaseSerialize(serializers.ModelSerializer):
    village = VillageSerialize()
    class Meta:
        model = Case
        fields = "__all__"