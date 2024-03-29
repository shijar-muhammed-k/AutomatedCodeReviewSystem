from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from .models import Profile, Payment


class ProfileSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, max_length=52, write_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 
                  'date_joined', 'phone', 'profile_image', 'profession', 'dob', 'gender']
        
    
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
