import imp
from rest_framework import serializers
from .models import ourusers

class ourusersSerialzers(serializers.ModelSerializer):
    class Meta:
        model = ourusers
        # fields = ('firstname', 'lastname')
        fields = '__all__'