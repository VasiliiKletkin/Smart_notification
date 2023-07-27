from bot.models import Telegram
from django.db import models
from django_currentuser.db.models import CurrentUserField
from resources.models import Resource


class Ticket(models.Model):
    created_by = CurrentUserField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name="Title")
    url = models.URLField(max_length=1024)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name="tickets")
    telegram = models.ForeignKey(
        Telegram,
        help_text='Input username without "@" or ID',
        on_delete=models.CASCADE,
        related_name="tickets",
    )

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        indexes = [
            models.Index(name="ticket_created_by_idx", fields=["created_by"]),
            models.Index(name="ticket_created_at_idx", fields=["created_at"]),
            models.Index(name="ticket_is_active_idx", fields=["is_active"]),
        ]

    def __str__(self):
        return f"{self.title} user:{self.created_by}"
