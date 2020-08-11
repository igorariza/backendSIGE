# Create your views here.

"""Serializers for the File"""
from .models import ImageResponse

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
    # Image
    ImageResponseSerializer,
    CreateImageResponseSerializer,
    DeleteImageResponseSerializer
    )

# ========== Feed ===================================================================================


# Listar todos los Secction
class ImageResponseList(ListAPIView):
    queryset = ImageResponse.objects.all()
    serializer_class = ImageResponseSerializer

# Listar un Secction
class ImageResponseDetail(RetrieveAPIView):
    queryset = ImageResponse.objects.all()
    serializer_class = ImageResponseSerializer

class ImageResponseCreate(ListCreateAPIView):
    queryset = ImageResponse.objects.all()
    serializer_class = CreateImageResponseSerializer

class ImageResponseDelete(DestroyAPIView):
    queryset = ImageResponse.objects.all()
    serializer_class = DeleteImageResponseSerializer
