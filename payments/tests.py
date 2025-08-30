from django.test import TestCase
from .models import Payment
from collect.models import Collect
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()

class PaymentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='payer', password='payerpass')
        self.collect = Collect.objects.create(
            creator=self.user,
            title='Wedding Fund',
            reason='wedding',
            description='Collection for a wedding party',
            target_amount=Decimal('5000.00'),
            current_amount=Decimal('1000.00'),
            end_date='2025-09-30 13:55:12',
        )
        self.payment = Payment.objects.create(
            payer=self.user,
            collect=self.collect,
            amount=Decimal('100.00'),
        )

    def test_payment_creation(self):
        self.assertEqual(self.payment.payer.username, 'payer')
        self.assertEqual(self.payment.collect.title, 'Wedding Fund')
        self.assertEqual(self.payment.amount, Decimal('100.00'))

    def test_payment_str(self):
        self.assertEqual(str(self.payment), 'payer - 100.00')