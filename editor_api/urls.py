from django.urls import path
from . import views

urlpatterns = [

        path("addconference/", AddConference.as_view(), name="addconference"),

]