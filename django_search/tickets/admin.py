from django.contrib import admin

from .forms import TicketForm
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
    )
    form = TicketForm

    def add_view(self, request, extra_content=None):
        self.fields = (
            "title",
            "url",
            "telegram",
            "is_active",
        )
        self.readonly_fields = ()
        return super().add_view(request, extra_context=extra_content)

    def change_view(self, request, object_id, extra_context=None):
        self.fields = (
            "title",
            "url",
            "telegram",
            "is_active",
            "created_by",
            "created_at",
        )
        self.readonly_fields = (
            "created_by",
            "created_at",
        )
        return super().change_view(request, object_id, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(created_by=request.user)
        return qs


admin.site.register(Ticket, TicketAdmin)
