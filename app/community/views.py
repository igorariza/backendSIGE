# Create your views here.

"""Serializers for the File"""
from .models import Community, Addfile, Replay

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
    # Community
    CommunitySerializer,
    CreateCommunitySerializer,
    UpdateCommunitySerializer,
    DeleteCommunitySerializer,
    # Addfile
    AddfileSerializer,
    DeleteAddfileSerializers,
    # Replay
    ReplaySerializer,
    CreateReplaySerializer,
    UpdateReplaySerializer,
    DeleteReplaySerializer,
)

# ========== Community ===================================================================================


# Listar todos los Secction
class ReplayList(ListAPIView):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer

# Listar un Secction


class ReplayDetail(RetrieveAPIView):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer

# Crear Secction


class ReplayCreate(ListCreateAPIView):
    queryset = Replay.objects.all()
    serializer_class = CreateReplaySerializer

# Actualizar datos de Secction por id


class ReplayUpdate(UpdateAPIView):
    queryset = Replay.objects.all()
    serializer_class = UpdateReplaySerializer

# Eliminar Un Secction sin afectar usuario


class ReplayDelete(DestroyAPIView):
    queryset = Replay.objects.all()
    serializer_class = DeleteReplaySerializer





class AddfileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data Addfile"""
        Addfile_serializer = AddfileSerializer(data=request.data)
        if Addfile_serializer.is_valid():
            """if the Addfile is full then save"""
            Addfile_serializer.save()
            return Response(Addfile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(Addfile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las Addfile
class AddfileList(ListAPIView):
    queryset = Addfile.objects.all()
    serializer_class = AddfileSerializer

# Listar un Addfile por id


class AddfileDetail(RetrieveAPIView):
    queryset = Addfile.objects.all()
    serializer_class = AddfileSerializer

 # Delete un Addfile por id


class AddfileDelete(DestroyAPIView):
    queryset = Addfile.objects.all()
    serializer_class = DeleteAddfileSerializers


class CommunityList(ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# Listar un Community por id


class CommunityDetail(RetrieveAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# Crear Community asignando un usuario ya existente


class CommunityCreate(ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CreateCommunitySerializer

# Actualizar datos de Community por id


class CommunityUpdate(UpdateAPIView):
    queryset = Community.objects.all()
    serializer_class = UpdateCommunitySerializer

# Eliminar Un Community sin afectar usuario


class CommunityDelete(DestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


# ========== upload to ProfilePicture ===================================================================================
class CommunityListbyIE(ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def get_queryset(self):
        Communitys = Community.objects.all().filter(
            user__codeIE=self.kwargs['codeIE'])
        return Communitys
