from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', )
    fields = ("title", "url", "telegram_username", "is_active", "telegram", "created_by")
    readonly_fields = ("telegram", "created_by")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(created_by=request.user)
        return qs

admin.site.register(Ticket, TicketAdmin)