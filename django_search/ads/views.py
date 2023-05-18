from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Ad
from .serializers import AdSerializer


class AdModelViewSet(ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_sent',]
    
    @action(detail=True, methods=['get'])
    def sent(self, request, pk=None):
        Ad.objects.filter(pk=pk).update(is_sent=True)
        # serializer = self.get_serializer(ad)
        return Response({"status": "success"})
   