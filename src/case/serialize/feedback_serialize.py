from rest_framework import serializers
from case.serialize.address_serialize import SubDistrictSerialize
from manage_users.models import Feedback
from manage_users.serializer.user_serialize import UserSerialize

class FeedbackSerialize(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ('created_at', 'updated_at')

class RetrevieFeedbackSerialize(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    sub_district = SubDistrictSerialize()
    class Meta:
        model = Feedback
        exclude = ('created_at', 'updated_at')

    def get_created_by(self, obj):
        return UserSerialize(obj.created_by).data

    
