from rest_framework.serializers import ModelSerializer
from .models import SuperType


class SuperTypeSerializer(ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type']
