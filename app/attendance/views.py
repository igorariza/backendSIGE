
"""Serializers for the File"""
from .models import *

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
from .serializers import *

# ========== Feed ===================================================================================


# Listar todos los Secction
class AttendanceList(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Listar un Secction
class AttendanceDetail(RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Crear Secction
class AttendanceCreate(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = CreateAttendanceSerializer

# Actualizar datos de Secction por id
class AttendanceUpdate(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = UpdateAttendanceSerializer

# Eliminar Un Secction sin afectar usuario
class AttendanceDelete(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = DeleteAttendanceSerializer
