from django.db.models import fields
from rest_framework import serializers
from case.models import Province, Regency, SubDistrict, Village

class ProvinceSerialize(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"

class RegencySerialize(serializers.ModelSerializer):
    class Meta:
        model = Regency
        fields = "__all__"

class SubDistrictSerialize(serializers.ModelSerializer):
    class Meta:
        model = SubDistrict
        fields = "__all__"

class VillageSerialize(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = "__all__"