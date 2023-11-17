from django.db.models import fields
from rest_framework import serializers
from case.models import Province, Regency, SubDistrict, Village

class ProvinceSerialize(serializers.ModelSerializer):
    class Meta:
        model = Province
        exclude = ('created_at', 'updated_at')

class RegencySerialize(serializers.ModelSerializer):
    class Meta:
        model = Regency
        exclude = ('created_at', 'updated_at')

class SubDistrictSerialize(serializers.ModelSerializer):
    class Meta:
        model = SubDistrict
        exclude = ('created_at', 'updated_at')

class VillageSerialize(serializers.ModelSerializer):
    class Meta:
        model = Village
        exclude = ('created_at', 'updated_at')