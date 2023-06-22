"""
    Views for editor api
"""
import os

from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.http import HttpResponse

from utils.utils import generate_token

from dotenv import load_dotenv, find_dotenv
from .serializers import AddConferenceSerializer, UserSerializer

load_dotenv(find_dotenv())


# Create your views here.

class AddConference(CreateAPIView):
    """
        Add new conference
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """ 
            Save New Conference Details
        """
        data = request.data.copy()
        serializer = AddConferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            status_code = status.HTTP_201_CREATED
            res = {"message": "new conference request added successfully"}
            send_user = User.objects.filter(id=serializer.data["created_by"])[0]

            subject, from_email, to_email = (
                f"New conference request from {send_user.first_name} {send_user.last_name}",
                os.environ.get("NO_REPLY_MAIL"),
                os.environ.get("ADMIN_EMAIL"),
            )
            text_content = "There is a new conference request"
            html_content = f"<p><b>Email:</b> {send_user.email}</p><p><b>Conference Name:</b> {serializer.data['title']}</p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return Response(res, status=status_code)
        return Response(serializer.errors)

class Registration(CreateAPIView):
    """ 
        User Registration
    """
    def post(self, request, *args, **kwargs):
        """
            Save User Registration Details
        """
        data = request.data.copy()
        serialized = UserSerializer(data=data)
        if serialized.is_valid():
            created_user = User.objects.create_user(
                username=data["username"],
                first_name=data["first_name"],
                email=data["email"],
                last_name=data["last_name"],
                is_active=False,
            )

            my_group = Group.objects.get(name="author")
            my_group.user_set.add(created_user)
            res = {"message": "Registration Successful."}

            send_activation_email(created_user, request)

            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

def send_activation_email(user, request):
    """Function to send activation email for registration

    Args:
        user (_type_): _description_
        request (_type_): _description_
    """
    current_site = get_current_site(request)
    subject, from_email, to_email = (
        f"New conference request from {user.first_name} {user.last_name}",
        os.environ.get("NO_REPLY_MAIL"),
        [user.email],
    )

    email_body = render_to_string(
        "authentication/activate.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=from_email,
        to=to_email,
    )
    email.send()


def activate_user(request, uidb64, token):
    """
        Activate User
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True
        user.save()
        template = loader.get_template("authentication/activate-succesful.html")
        return HttpResponse(template.render(request=request))
    else:
        template = loader.get_template("authentication/activate-failed.html")
        return HttpResponse(template.render(request=request))
