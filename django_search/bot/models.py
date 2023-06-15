from django.db import models


class Telegram(models.Model):
    user_id = models.CharField(max_length=32, unique=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Telegram profile"
        verbose_name_plural = "Telegram profiles"

    def __str__(self):
        return f"{self.username}-{self.user_id}, {self.first_name} {self.last_name}"
