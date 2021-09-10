from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from notes.models import Notes
from .serializers import NotesSerializer
from rest_framework import status
from rest_framework.views import APIView


class NotesAPIView(APIView):

    def get(self):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.date)

    def post(self, id):
        serializer = NotesSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors)