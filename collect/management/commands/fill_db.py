from django.core.management.base import BaseCommand
from collect.models import Collect  
from django.contrib.auth import get_user_model
from faker import Faker  
import random
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Наполнить БД моковыми данными'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = [User.objects.create_user(username=fake.user_name(), password='password') for _ in range(10)]

        for _ in range(1000):  # Создаем 1000 моковых записей
            Collect.objects.create(
                creator=random.choice(users),
                title=fake.sentence(),  
                reason='моковая причина',
                description=fake.text(),
                target_amount=Decimal(random.randint(100, 10000)),  # Случайная сумма от 100 до 10000
                current_amount=Decimal(0.00),
                end_date=fake.date_time_between(start_date='now', end_date='+30d'),  
            )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена моковыми данными.'))