from django.apps import AppConfig


class EditorApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "editor_api"

class ConferenceApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "conference_api"
