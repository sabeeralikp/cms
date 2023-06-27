""" To display Conference models in Django admin panel
"""
from django.contrib import admin

from conference.models.conference_models import Conference


# Register your models here.
admin.site.register(Conference)
