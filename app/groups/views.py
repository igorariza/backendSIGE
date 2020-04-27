# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Group

from .serializers import (
    GroupSerializer,
    CreateGroupSerializer,
    UpdateGroupSerializer,
    DeleteGroupSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response



# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los Group
class GroupList(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Listar un Group
class GroupDetail(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Crear Group 
class GroupCreate(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = CreateGroupSerializer

# Actualizar datos de Group por id
class GroupUpdate(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = UpdateGroupSerializer

# Eliminar Un Group sin afectar usuario
class GroupDelete(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class =  DeleteGroupSerializer
