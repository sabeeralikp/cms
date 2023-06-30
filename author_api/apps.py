"""
    To load Author App
"""
from django.apps import AppConfig


class AuthorApiConfig(AppConfig):
    """Class for Author API Configuaration

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "author_api"
