import json
from django.shortcuts import render
from .serializers import (  TeacherProfileSerializer,
                            TeacherBilingInformationSerializer,
                            TeachAvailabilitySerializer,
                            TeacherSubjectSerializer,
                            TeacherIDCardSerializer,
                            TeacherLicencesSerializer,
                            TeacherCertificateSerializer,
                            TeacherVedioSerializer
                            
                    )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.http import Http404

class TeacherInfoView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        teacher =TeacherInfo.objects.all()
        serializer = TeacherProfileSerializer(teacher, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeacherProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class TeacherdetailInfoView(APIView):
    """
    Retrieve, update or delete a Teacher instance.
    """
    def get_object(self, pk):
        try:
            return TeacherInfo.objects.get(pk=pk)
        except TeacherInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teach_info = self.get_object(pk)
        serializer = TeacherProfileSerializer(teach_info)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teach_info = self.get_object(pk)
        serializer = TeacherProfileSerializer(teach_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teach_info = self.get_object(pk)
        teach_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherBilingInfoView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        teacher = BilingInformation.objects.all()
        serializer = TeacherBilingInformationSerializer(teacher, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        
        serializer = TeacherBilingInformationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class TeacherBilingdetailView(APIView):
    """
    Retrieve, update or delete a Teacher biling  instance.
    """
    def get_object(self, pk):
        try:
            return BilingInformation.objects.get(pk=pk)
        except BilingInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        biling_info = self.get_object(pk)
        serializer = BilingInformation(biling_info)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        biling_info = self.get_object(pk)
        serializer = BilingInformation(biling_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        biling_info = self.get_object(pk)
        biling_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeachAvailabilityView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        availability =TeachAvailability.objects.all()
        serializer = TeachAvailabilitySerializer(availability, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeachAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class TeachAvailabilitydetailView(APIView):
    """
    Retrieve, update or delete a teacher Subject instance.
    """
    def get_object(self, pk):
        try:
            return TeachAvailability.objects.get(pk=pk)
        except TeachAvailability.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        availability = self.get_object(pk)
        serializer = TeachAvailabilitySerializer(availability)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        availability = self.get_object(pk)
        serializer = TeachAvailabilitySerializer(availability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        availability = self.get_object(pk)
        availability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeachSubjectView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        availability =TeachAvailability.objects.all()
        serializer = TeacherSubjectSerializer(availability, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeacherSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeachSubjectdetailView(APIView):
    """
    Retrieve, update or delete a teacher subject instance.
    """
    def get_object(self, pk):
        try:
            return TeacherSubject.objects.get(pk=pk)
        except TeacherSubject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teachsubject = self.get_object(pk)
        serializer = TeacherSubjectSerializer(teachsubject)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teachsubject = self.get_object(pk)
        serializer = TeacherSubjectSerializer(teachsubject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teachsubject = self.get_object(pk)
        teachsubject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeachIDCardView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        id_card =TeacherInfo.objects.all()
        serializer = TeacherIDCardSerializer(id_card, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeacherIDCardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeachIDCarddetailView(APIView):
    """
    Retrieve, update or delete a teacher id card instance.
    """
    def get_object(self, pk):
        try:
            return TeacherInfo.objects.get(pk=pk)
        except TeacherInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teach_id_card = self.get_object(pk)
        serializer = TeacherIDCardSerializer(teach_id_card)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teach_id_card = self.get_object(pk)
        serializer = TeacherIDCardSerializer(teach_id_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teach_id_card = self.get_object(pk)
        teach_id_card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeachLicencesView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        teach_licences =TeacherInfo.objects.all()
        serializer = TeacherLicencesSerializer(teach_licences, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeacherLicencesSerializer(data=request.data)
        import pdb;pdb.set_trace() 
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeachLicencesdetailView(APIView):
    """
    Retrieve, update or delete a teacher licences instance.
    """
    def get_object(self, pk):
        try:
            return TeacherInfo.objects.get(pk=pk)
        except TeacherInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teach_licences = self.get_object(pk)
        serializer = TeacherLicencesSerializer(teach_licences)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teach_licences = self.get_object(pk)
        serializer = TeacherLicencesSerializer(teach_licences, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teach_licences = self.get_object(pk)
        teach_licences.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

class TeachVedioView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        teach_vedio =TeacherInfo.objects.all()
        serializer = TeacherVedioSerializer(teach_vedio, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeacherVedioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeachVediodetailView(APIView):
    """
    Retrieve, update or delete a teacher vedio instance.
    """
    def get_object(self, pk):
        try:
            return TeacherInfo.objects.get(pk=pk)
        except TeacherInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teach_vedio = self.get_object(pk)
        serializer = TeacherVedioSerializer(teach_vedio)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teach_vedio = self.get_object(pk)
        serializer = TeacherVedioSerializer(teach_vedio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teach_vedio = self.get_object(pk)
        teach_vedio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 

class TeachCertificateView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request):
        teach_certificate =TeacherInfo.objects.all()
        serializer = TeacherCertificateSerializer(teach_certificate, many=True)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        
        serializer = TeacherCertificateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TeachCertificatedetailView(APIView):
    """
    Retrieve, update or delete a teacher certificate instance.
    """
    def get_object(self, pk):
        try:
            return TeacherInfo.objects.get(pk=pk)
        except TeacherInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teach_certificate = self.get_object(pk)
        serializer = TeacherCertificateSerializer(teach_certificate)
        return Response({"success": "True", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teach_certificate = self.get_object(pk)
        serializer = TeacherCertificateSerializer(teach_certificate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "True", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teach_certificate = self.get_object(pk)
        teach_certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)