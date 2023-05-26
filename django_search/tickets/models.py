from urllib.parse import unquote

from django.core.exceptions import ValidationError
from django.db import models
from django_currentuser.db.models import CurrentUserField
from profiles.models import Telegram


class Ticket(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    url = models.URLField(max_length=1024)
    telegram_username = models.CharField(max_length=30, verbose_name="Telegram")
    created_by = CurrentUserField()
    is_active = models.BooleanField(default=True, verbose_name="Active")
    telegram = models.ForeignKey(Telegram, blank=True, null=True, on_delete=models.CASCADE, related_name="tickets")
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    
    def __str__(self):
        return f"{self.title} user:{self.created_by}"
    
    def save(self, *args, **kwargs) -> None:
        self.url = unquote(self.url)
        return super().save(*args, **kwargs)
    
    def clean(self):
        tg = Telegram.objects.filter(username=self.telegram_username)
        if not tg.exists():
            raise ValidationError({'telegram_username': "Back to Telegram Bot"})
        self.telegram = tg.first()
        return super().clean()