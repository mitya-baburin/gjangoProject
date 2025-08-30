from rest_framework import serializers
from .models import Collect
from django.contrib.auth import get_user_model

User = get_user_model()

class CollectSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Collect
        fields = '__all__'

    def validate_target_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Целевая сумма должна быть больше нуля.")
        return value