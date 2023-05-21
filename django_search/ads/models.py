from django.db import models
from tickets.models import Ticket


class Ad(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="ads")
    url = models.URLField(max_length=1024)
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    is_sent = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not Ad.objects.filter(url=self.url, ticket=self.ticket).exists():
            return super().save(*args, **kwargs)

