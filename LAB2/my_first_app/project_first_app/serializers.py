from rest_framework import serializers
from .models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'last_name', 'first_name', 'birth_date')
