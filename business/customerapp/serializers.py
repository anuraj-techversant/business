"""
The serializers.py contain various serializer classes under customer app
"""
from customerapp.models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    """
    The serializer method for Customer model.
    """
    class Meta:
        model = Customer
        fields = '__all__'
