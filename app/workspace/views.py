# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import WorkSpace

from .serializers import (
    WorkSpaceSerializer,
    CreateWorkSpaceSerializer,
    UpdateWorkSpaceSerializer,
    DeleteWorkSpaceSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response



# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los WorkSpace
class WorkSpaceList(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer

# Listar un WorkSpace
class WorkSpaceDetail(RetrieveAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer

# Crear WorkSpace 
class WorkSpaceCreate(ListCreateAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = CreateWorkSpaceSerializer

# Actualizar datos de WorkSpace por id
class WorkSpaceUpdate(UpdateAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = UpdateWorkSpaceSerializer

# Eliminar Un WorkSpace sin afectar usuario
class WorkSpaceDelete(DestroyAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class =  DeleteWorkSpaceSerializer
