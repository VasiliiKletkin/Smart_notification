from django.contrib import admin
from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resource, ResourceAdmin)
