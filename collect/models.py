from django.core.mail import send_mail
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Collect(models.Model):
    EVENT_CHOICES = [
        ('birthday', 'День рождения'),
        ('wedding', 'Свадьба'),
        ('other', 'Другое'),
    ]

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=255)
    reason = models.CharField(max_length=50, choices=EVENT_CHOICES)
    description = models.TextField(blank=True)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cover_image = models.ImageField(upload_to='covers/')
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Payment(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE, related_name='donations')
    related_name='collector',  
    on_delete=models.CASCADE
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.payer} - {self.amount}"    
    

    def save(self, *args, **kwargs):
       
        if self.pk is None:
            
            super().save(*args, **kwargs)
            
            send_mail(
                'Создан новый сбор',
                f'Сбор "{self.title}" успешно создан.',
                'mityababurin@gmail.com',  
                [self.creator.email], 
                fail_silently=False,
            )
        else:
            
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title    