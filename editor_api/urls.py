from django.urls import path
from . import views

app_name = "editor_api"
urlpatterns = [
    path("addconference/", views.AddConference.as_view(), name="addconference"),
    path("registration/", views.Registration, name="registration"),
    path("activate-user/<uidb64>/<token>", views.activate_user, name="activate"),
]
