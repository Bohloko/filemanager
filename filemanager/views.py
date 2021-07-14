from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import generics
from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
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

    def destroy(self, request, pk):
        print("debug: " + pk)
        if(request.method == 'DELETE'):
            ApplicationFile.objects.get(id = pk).delete()
            return Response('file deleeeeted')
        return Response('failed to delete')



class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class FileSearchView(generic.View):

    def get(self, request):
        search_word = str(request.GET.get('search_word'))
        # get all files
        files = ApplicationFile.objects.all()
        response = {} # filename: word_occurance
        for file in files:
            occurance = 0
            file_content = str(file.file_content)
            word_list = file_content[2:len(file_content)-1].split(' ')
            for word in word_list: 
                if word.lower() == search_word.lower():
                    occurance = occurance + 1

            response[str(file.filename)] = occurance
        
        response = sorted(response.items(), key= lambda item: item[1], reverse=True)
        print(response)
        return JsonResponse({'data': response})

@api_view(['DELETE'])
def file_delete(request, pk):
    file = ApplicationFile.objects.get(id = pk)
    file.delete()
    return Response('File successfully Deleted')
