from rest_framework import serializers
from teacher.models import *

class AddUniversitySerializer(serializers.ModelSerializer):
    """
    Serializer for University endpoint.
    """

    class Meta:
        model = University
        fields ='__all__'