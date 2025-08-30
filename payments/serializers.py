from rest_framework import serializers
from .models import Payment
from collect.models import Collect

class PaymentSerializer(serializers.ModelSerializer):
    payer = serializers.ReadOnlyField(source='payer.username')

    class Meta:
        model = Payment
        fields = '__all__'
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Сумма платежа должна быть больше нуля.")
        return value
    
    def validate(self, attrs):
        collect = attrs['collect']
        if collect.current_amount + attrs['amount'] > collect.target_amount:
            raise serializers.ValidationError("Сумма не должна превышать целевую сумму сбора.")
        return attrs