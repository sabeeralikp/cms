"""
    To load Conference App
"""
from django.apps import AppConfig


class ConferenceConfig(AppConfig):
    """Class for Conference API Configuaration

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "conference"
