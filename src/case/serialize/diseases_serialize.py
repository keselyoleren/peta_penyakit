from rest_framework import serializers
from case.models import Disease

class DiseasesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Disease
        exclude = ('created_at', 'updated_at')