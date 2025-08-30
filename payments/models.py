from django.core.mail import send_mail
from django.db import models
from django.contrib.auth import get_user_model
from collect.models import Collect



User = get_user_model()

class Payment(models.Model):
    collect = models.ForeignKey(
        Collect, 
        related_name='payment_payments',  # Уникальное имя для обратного доступа
        on_delete=models.CASCADE
    )
    payer = models.ForeignKey(
        User, 
        related_name='payment_payments_received',  # Уникальное имя для обратного доступа
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.payer} - {self.amount}"    
    
    def save(self, *args, **kwargs):
       
        if self.pk is None:
            
            super().save(*args, **kwargs)
            
            send_mail(
                'Платеж успешно отправлен',
                f'Платеж в размере {self.amount} успешно обработан для сбора "{self.collect.title}".',
                'mityababurin@gmail.com',  
                [self.payer.email],  
                fail_silently=False,
            )
        else:
          
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.payer.username} - {self.amount}"