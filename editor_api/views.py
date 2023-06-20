from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddConferenceSerializer
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


# Create your views here.

# ----- ADD NEW CONFERENCE
class AddConference(CreateAPIView):
    """
    Add new conference
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        serializer = AddConferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            status_code = status.HTTP_201_CREATED
            res = {"message": "new conference request added successfully"}
            send_user = User.objects.filter(id=serializer.data['created_by'])[0]

            subject, from_email, to = f"New conference request from {send_user.first_name} {send_user.last_name}", os.environ.get("NO_REPLY_MAIL"), os.environ.get("ADMIN_EMAIL")
            text_content = "There is a new conference request"
            html_content = f"<p><b>Email:</b> {send_user.email}</p><p><b>Conference Name:</b> {serializer.data['title']}</p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return Response(res, status=status_code)
        return Response(serializer.errors)