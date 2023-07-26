from typing import Any
from django.contrib import admin
from resources.models import Resource
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
        return super().add_view(request)

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
        return super().change_view(request, object_id)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(created_by=request.user)
        return qs

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        hostname = obj.url.split("://")[1].split("/")[0]
        obj.resource = Resource.objects.get(url__icontains=hostname)
        return super().save_model(request, obj, form, change)
    

admin.site.register(Ticket, TicketAdmin)
