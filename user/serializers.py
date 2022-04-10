from rest_framework import serializers

from user.models import *




class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for Regiter User endpoint.
    """
    email = serializers.EmailField(
        required=True,
    )

    password = serializers.CharField(write_only=True, required=True)
    confrim_password = serializers.CharField(write_only=True, required=True)

    
    

    def validate(self, attrs):
        if attrs['password'] != attrs['confrim_password']:
            
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if int(attrs['mobile']) < 10: 
            
            raise serializers.ValidationError({"Mobile no": "no  should be  10 digit."})

        return attrs  

        

    def create(self, validated_data):
     
        user = User.objects.create(
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        email=validated_data['email'],
        gender=validated_data['gender'],
        mobile=validated_data['mobile'],
        location=validated_data['location'],
        user_role = validated_data['user_role'],
        country = validated_data['country'],
        otp=validated_data['otp'],
        image = validated_data['image']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

class VerifyOtpSerializer(serializers.ModelSerializer):
    """
    Serializer for Verify OTP endpoint.
    """

    class Meta:
        model = User
        fields = (  'mobile','otp' )

class EditUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'