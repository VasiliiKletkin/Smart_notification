from urllib.parse import unquote

from bot.models import Telegram
from django.db import models
from django_currentuser.db.models import CurrentUserField


class Ticket(models.Model):
    created_by = CurrentUserField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name="Title")
    url = models.URLField(max_length=1024)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    telegram = models.ForeignKey(
        Telegram,
        help_text='Input username without "@" or ID',
        on_delete=models.CASCADE,
        related_name="tickets",
    )

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"{self.title} user:{self.created_by}"

    def save(self, *args, **kwargs) -> None:
        self.url = unquote(self.url)
        return super().save(*args, **kwargs)
