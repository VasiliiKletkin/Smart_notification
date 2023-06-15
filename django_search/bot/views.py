from dal import autocomplete
from django.db.models import Q

from .models import Telegram


class TelegramAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Telegram.objects.all()
        if self.q:
            return qs.filter(Q(user_id=self.q) | Q(username=self.q))
        return []
