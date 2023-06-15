from django.contrib import admin
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_sent')
    fields = ('title','ticket', 'url', 'created_at','is_sent')
    readonly_fields = ('created_at',)
    
admin.site.register(Ad, AdAdmin)
