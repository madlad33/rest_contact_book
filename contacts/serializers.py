from  rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    """Serializes Contact model"""
    class Meta:
        model = contacts
        fields = ['name','email','mobile_no','address']

