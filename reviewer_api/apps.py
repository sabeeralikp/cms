"""
    To load Reviewer App
"""
from django.apps import AppConfig


class ReviewerApiConfig(AppConfig):
    """Class for Reviewer API Configuaration

    Args:
        AppConfig (_type_): _description_
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "reviewer_api"
