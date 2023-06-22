from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import Group, Permission

# Create your models here.


class Conference(models.Model):
    """Model for conference

    Args:
        models (_type_): _description_
    """

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50, unique=True)
    tracks = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    is_verified_by_admin = models.BooleanField()
    conference_website = models.CharField(max_length=250)

    class Meta:
        db_table = "conference"


# new_group = Group(name="Editors")
# new_group.save()
