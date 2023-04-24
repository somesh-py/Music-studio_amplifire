from rest_framework import serializers
from ..models import MusicReg


class MusicRegSerializer(serializers.ModelSerializer):
    class Meta:
        model=MusicReg
        fields='__all__'