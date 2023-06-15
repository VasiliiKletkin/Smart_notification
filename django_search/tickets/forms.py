from dal import autocomplete
from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        widgets = {
            "telegram": autocomplete.ModelSelect2(url="telegram-autocomplete"),
        }
