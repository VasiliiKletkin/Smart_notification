from django.db import models
from urllib.parse import unquote
from django_currentuser.db.models import CurrentUserField


class Ticket(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    url = models.URLField(max_length=1024)
    telegram_id = models.CharField(max_length=30, verbose_name="Telegram")
    created_by = CurrentUserField()
    is_active = models.BooleanField(default=False, verbose_name="Active")

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    
    def __str__(self):
        return f"{self.title} user:{self.created_by}"
    
    def save(self, *args, **kwargs) -> None:
        self.url = unquote(self.url)
        return super().save(*args, **kwargs)
    