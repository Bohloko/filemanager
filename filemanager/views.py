from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UploadSerializer, ApplicationFileSerializer, UserSerializer
from .models import ApplicationFile

class FileUploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response('GET API')

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        ApplicationFile.objects.create(
            filename = file_uploaded.name,
            file_content = file_uploaded.read(),
            file_size = file_uploaded.size
        )
        return Response("file uploaded successfully")

class ApplicationFileViewSet(ModelViewSet):
    queryset = ApplicationFile.objects.all()
    serializer_class = ApplicationFileSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer