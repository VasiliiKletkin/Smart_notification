from django.contrib import admin

from .models import Telegram


class TelegramAdmin(admin.ModelAdmin):
    list_display = ("user_id", "username", "first_name", "last_name")
    search_fields = ("user_id", "username", "first_name", "last_name")
    readonly_fields = ("user_id", "created_at")

admin.site.register(Telegram, TelegramAdmin)
