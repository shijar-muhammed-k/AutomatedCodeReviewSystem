from rest_framework import serializers
from .models import Code, AdminCredits

class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = '__all__'
        depth = 1
        
        
class AdminBalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminCredits
        fields = '__all__'
        depth = 1