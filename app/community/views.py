# Create your views here.

"""Serializers for the File"""
from .models import Community

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

from rest_framework import status
from .serializers import (
    # Community
    CommunitySerializer,
    CreateCommunitySerializer,
    UpdateCommunitySerializer,
    DeleteCommunitySerializer
    )

# ========== Community ===================================================================================


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
    serializer_class = CreateCommunitySerializer
    
    def get_queryset(self):
        Communitys = Community.objects.all().filter(
            user__codeIE=self.kwargs['codeIE'])
        return Communitys
        
        