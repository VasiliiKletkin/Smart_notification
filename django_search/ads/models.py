from django.db import models
from tickets.models import Ticket


class Ad(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="ads")
    url = models.URLField(max_length=1024)
    title = models.CharField(max_length=255)
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        indexes = [
            models.Index(name="ad_url_idx", fields=["url"]),
            models.Index(name="ad_is_sent_idx", fields=["is_sent"]),
            models.Index(name="ad_created_at_idx", fields=["created_at"]),
        ]

    def __str__(self) -> str:
        return f"{self.title}, {self.created_at}"

    def save(self, *args, **kwargs):
        if not Ad.objects.filter(url=self.url, ticket=self.ticket).exists():
            return super().save(*args, **kwargs)
