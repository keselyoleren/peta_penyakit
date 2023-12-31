from django.db.models import fields
from rest_framework import serializers
from case.models import Province, Regency, SubDistrict, Village
from manage_users.models import Puskeswan

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

class SubDistrictPuskeswanSerialize(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    puskeswan = serializers.SerializerMethodField()
    
    class Meta:
        model = SubDistrict
        fields = ('id', 'name', 'puskeswan','count')

    def get_puskeswan(self, obj):
        try:
            pus = Puskeswan.objects.filter(wilayah_pelayanan=obj.id).first()
            return {
                'id': pus.id,
                'name': pus.name,
            }
        except:
            return {
                'id': None,
                'name': None,
            }
    
    def get_count(self, obj):
        return {
            'villages': Village.objects.filter(sub_district=obj.id).count()
        }


class VillageSerialize(serializers.ModelSerializer):
    class Meta:
        model = Village
        exclude = ('created_at', 'updated_at')

class SubDistrictAndVillagePuskeswanSerialize(serializers.ModelSerializer):
    villages = serializers.SerializerMethodField()
    class Meta:
        model = SubDistrict
        fields = ('id', 'name', 'villages')

    def get_villages(self, obj):
        village =  Village.objects.filter(sub_district=obj.id)
        return VillageSerialize(village, many=True).data


class VillageDtetailSerialize(serializers.ModelSerializer):
    sub_district = SubDistrictPuskeswanSerialize()
    class Meta:
        model = Village
        exclude = ('created_at', 'updated_at')