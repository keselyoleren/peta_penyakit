from rest_framework import serializers
from case.models import Case, Village
from case.serialize.address_serialize import VillageDtetailSerialize
from case.serialize.diseases_serialize import DiseasesSerialize

class CaseSerialize(serializers.ModelSerializer):
    village = VillageDtetailSerialize()
    diseases = DiseasesSerialize()
    class Meta:
        model = Case
        fields = "__all__"