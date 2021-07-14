
from rest_framework.serializers import Serializer, FileField, ModelSerializer
from django.contrib.auth import get_user_model
from .models import ApplicationFile

class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded',]

class ApplicationFileSerializer(ModelSerializer):
    class Meta:
        model = ApplicationFile
        fields = ['id', 'filename', 'upload_date', 'file_size', 'file_content']

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']