from django.contrib import admin
from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'is_sent')
    
admin.site.register(Ad, AdAdmin)
