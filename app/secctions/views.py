# Create your views here.

"""Serializers for the Resource"""
from .models import (
    Resource,
    Secction,
    HyperLynks
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
    # Resource
    ResourceSerializer,
    DeleteResourceSerializers,
    # Hyperlyncs
    HyperLynksSerializer,
    CreateHyperLynksSerializer,
    UpdateHyperLynksSerializer,
    DeleteHyperLynksSerializer,
    # Secction
    SecctionSerializer,
    CreateSecctionSerializer,
    UpdateSecctionSerializer,
    DeleteSecctionSerializer
)



# ========== upload to Resource ===================================================================================
class ResourceUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data Resource"""
        Resource_serializer = ResourceSerializer(data=request.data)

        if Resource_serializer.is_valid():
            """if the Resource is full then save"""
            Resource_serializer.save()
            return Response(Resource_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(Resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las Resource
class ResourceList(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# Listar un Resource por id


class ResourceDetail(RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

 # Delete un Resource por id


class ResourceDelete(DestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = DeleteResourceSerializers

# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los HyperLynks
class HyperLynksList(ListAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = HyperLynksSerializer

# Listar un HyperLynks
class HyperLynksDetail(RetrieveAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = HyperLynksSerializer

# Crear HyperLynks 
class HyperLynksCreate(ListCreateAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = CreateHyperLynksSerializer

# Actualizar datos de HyperLynks por id
class HyperLynksUpdate(UpdateAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = UpdateHyperLynksSerializer

# Eliminar Un HyperLynks sin afectar usuario
class HyperLynksDelete(DestroyAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class =  DeleteHyperLynksSerializer

# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los Secction
class SecctionList(ListAPIView):
    queryset = Secction.objects.all()
    serializer_class = SecctionSerializer

# Listar un Secction
class SecctionDetail(RetrieveAPIView):
    queryset = Secction.objects.all()
    serializer_class = SecctionSerializer

# Crear Secction 
class SecctionCreate(ListCreateAPIView):
    queryset = Secction.objects.all()
    serializer_class = CreateSecctionSerializer

# Actualizar datos de Secction por id
class SecctionUpdate(UpdateAPIView):
    queryset = Secction.objects.all()
    serializer_class = UpdateSecctionSerializer

# Eliminar Un Secction sin afectar usuario
class SecctionDelete(DestroyAPIView):
    queryset = Secction.objects.all()
    serializer_class =  DeleteSecctionSerializer
