from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddConferenceSerializer
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
            res = {"msg": "new conference added successfully"}
            return Response(res, status=status_code)
        return Response(serializer.errors)