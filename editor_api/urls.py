from django.urls import path
from . import views

urlpatterns = [

        path("addconference/", views.AddConference.as_view(), name="addconference"),

]