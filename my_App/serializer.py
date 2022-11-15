from rest_framework import serializers
from .models import Fan


class FansSerializer(serializers.ModelSerializer):
    class Meta:
        medel = Fan
        field = ['id', 'username', 'email', 'password']