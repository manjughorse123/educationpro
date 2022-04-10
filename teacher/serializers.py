from rest_framework import serializers
from .models import *

class TeacherProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for TeaherInfo endpoint.
    """
    
    class Meta:
        model = TeacherInfo
        fields ='__all__'


class TeacherBilingInformationSerializer(serializers.ModelSerializer):
    """
    Serializer for TeaherInfo endpoint.
    """
    class Meta:
        model = BilingInformation
        fields ='__all__'

# class SelectFieldSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SelectField
#         fields = ['day','time']

# class TeachAvailabilitySerializer(serializers.ModelSerializer):
#     availability = SelectFieldSerializer()

#     class Meta:
#         model = TeachAvailability
#         fields = ['user','availability']

#     def create(self, validated_data):
#         import pdb;pdb.set_trace()
#         availability = validated_data.pop('availability')
#         user = TeachAvailability.objects.create(**validated_data)
        
#         SelectField.objects.create(user=user, **availability)
#         return user



class TeachAvailabilitySerializer(serializers.ModelSerializer):
    """
    Serializer for TeaherInfo endpoint.
    """
    class Meta:
        model = TeachAvailability
        fields ='__all__'



class TeacherSubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Teaher subject endpoint.
    """
    class Meta:
        model = TeacherSubject
        fields ='__all__'


class TeacherLicencesSerializer(serializers.ModelSerializer):
    """
    Serializer for Teacher licencese endpoint.
    """
    teach_licences = serializers.URLField(required=True )
    class Meta:
        model = TeacherInfo
        fields = ['teach_licences','user']
        
       
    
    def create(self, validated_data):
        teach_licences, created = TeacherInfo.objects.update_or_create(
            user=validated_data.get('user', None),
            defaults={'teach_licences': validated_data.get('teach_licences', None)})

        return teach_licences


class TeacherVedioSerializer(serializers.ModelSerializer):
    """
    Serializer for Teacher vedio endpoint.
    """
    teach_vedio = serializers.URLField(required=True, )
    class Meta:
        model = TeacherInfo
        fields = ['teach_vedio','user']
    
    def create(self, validated_data):
        teach_vedio, created = TeacherInfo.objects.update_or_create(
            user=validated_data.get('user', None),
            defaults={'teach_vedio': validated_data.get('teach_vedio', None)})

        return teach_vedio

class TeacherIDCardSerializer(serializers.ModelSerializer):
    """
    Serializer for Teacher IdCard endpoint.
    """
    teach_idcard = serializers.URLField(required=True, )
    class Meta:
        model = TeacherInfo
        fields = ['teach_idcard','user']

    def create(self, validated_data):
        teach_idcard, created = TeacherInfo.objects.update_or_create(
            user=validated_data.get('user', None),
            defaults={'teach_idcard': validated_data.get('teach_idcard', None)})

        return teach_idcard

class TeacherCertificateSerializer(serializers.ModelSerializer):
    """
    Serializer for Teacher Certificate endpoint.
    """
    teach_certificate = serializers.URLField(required=True, )
    class Meta:
        model = TeacherInfo
        fields = ['teach_certificate','user']
        
    def create(self, validated_data):
        teach_certificate, created = TeacherInfo.objects.update_or_create(
            user=validated_data.get('user', None),
            defaults={'teach_certificate': validated_data.get('teach_certificate', None)})

        return teach_certificate