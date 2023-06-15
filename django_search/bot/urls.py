from django.urls import include, path

from .views import TelegramAutocomplete

urlpatterns = [
    path(
        "telegram-autocomplete/",
        TelegramAutocomplete.as_view(),
        name="telegram-autocomplete",
    ),
]
