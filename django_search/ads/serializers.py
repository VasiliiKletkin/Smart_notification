from rest_framework import serializers
from tickets.serializers import TicketSerializer

from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer()
    class Meta:
        model = Ad
        fields = "__all__"
