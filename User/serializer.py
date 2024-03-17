from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from .models import Profile, Payment, Messages

class ProfileSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, max_length=52, write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 
                  'date_joined', 'phone', 'profile_image', 'profession', 'dob', 'gender', 'credit_points', 'role']
        
    
    def create(self, validated_data):
        password = make_password(validated_data.pop("password"))
        validated_data['password'] = password
        return super().create(validated_data)
    

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        amount = validated_data.get("amount")
        profile = self.context['request'].user.profile
        profile.credit_points += amount
        profile.save()
        return super().create(validated_data)


class UserTokenObtainSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        user = get_object_or_404(Profile, email = attrs.pop('username'))
        print(user)
        attrs['username'] = user.username
        data = super().validate(attrs)
        profile = Profile.objects.filter(username=self.user).first()
        
        print(data)
        
        return {
            "access": data['access'],
            "role": profile.role,
            "id": profile.id
        }
        
        

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Messages
        fields = '__all__'
        depth = 1