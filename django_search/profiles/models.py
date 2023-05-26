from django.db import models


class Telegram(models.Model):
    telegram_id = models.CharField(
        'telegram_id', max_length=20, unique=True)
    username = models.CharField(
        'username', max_length=20)
    
    def __str__(self):
        return f'{self.username}-{self.telegram_id}'