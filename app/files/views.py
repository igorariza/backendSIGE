# Create your views here.

"""Serializers for the File"""
from .models import (
    File,
    Evidence
    )
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .serializers import (
    # File
    FileSerializer,
    DeleteFileSerializers,
    # Evidence
    EvidenceSerializer,
    CreateEvidenceSerializer,
    UpdateEvidenceSerializer,
    DeleteEvidenceSerializer
    )


# ========== upload to file ===================================================================================
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data file"""
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            """if the file is full then save"""
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las File
class FileList(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

# Listar un File por id


class FileDetail(RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

 # Delete un File por id


class FileDelete(DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = DeleteFileSerializers

# ========== Evidence ===================================================================================


class EvidenceList(ListAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

# Listar un Evidence por id


class EvidenceDetail(RetrieveAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

# Crear Evidence asignando un usuario ya existente


class EvidenceCreate(ListCreateAPIView):
    queryset = Evidence.objects.all()
    serializer_class = CreateEvidenceSerializer

# Actualizar datos de Evidence por id


class EvidenceUpdate(UpdateAPIView):
    queryset = Evidence.objects.all()
    serializer_class = UpdateEvidenceSerializer

# Eliminar Un Evidence sin afectar usuario


class EvidenceDelete(DestroyAPIView):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer


# ========== upload to ProfilePicture ===================================================================================
