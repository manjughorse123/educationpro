from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import *     
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teacher.models import *
from django.http import Http404

class AddUniversityView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        availability = University.objects.all()
        serializer = AddUniversitySerializer(availability, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = AddUniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddUniversitydetailView(APIView):
    """
    Retrieve, update or delete a teacher subject instance.
    """
    def get_object(self, pk):
        try:
            return University.objects.get(pk=pk)
        except University.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        adduniversity = self.get_object(pk)
        serializer = AddUniversitySerializer(adduniversity)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        adduniversity = self.get_object(pk)
        serializer = AddUniversitySerializer(adduniversity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        adduniversity = self.get_object(pk)
        adduniversity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
