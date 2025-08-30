from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(payer=self.request.user)
        # Можно обновлять текущую сумму сбора
        collect = serializer.validated_data['collect']
        collect.current_amount += serializer.validated_data['amount']
        collect.save()