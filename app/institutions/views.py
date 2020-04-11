# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework.permissions import IsAdminUser, BasePermission
from .models import EducationalInstitution, Headquarters
from users.models import StaffUser


from institutions.serializers import (
    EducationalInstitutionSerializer,
    UpdateEducationalInstitutionSerializer,
    CreateEducationalInstitutionSerializer,
    InactivateEducationalInstitutionSerializer,
    DeleteEducationalInstitutionSerializer,
    HeadquartersSerializer,
    CreateHeadquartersSerializer,
    UpdateHeadquartersSerializer,
    InactivateHeadquartersSerializer,
    DeleteHeadquartersSerializer
)

from rest_framework.views import APIView
from rest_framework.response import Response


""" ===================================================
Las siguientes clases verifican si quien consulta una ruta
tiene el cargo para poder hacer dicha consulta.
"""

class AllowPrincipal(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 1)
        else:
            return False

class AllowSubprincipal(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 2)
        else:
            return False


class AllowPayer(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 3)
        else:
            return False
        
class AllowAssistant(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 4)
        else:
            return False

class AllowAssistantSIMAT(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 5)
        else:
            return False
        
# ========== CRUD para la informacion basica de la Educational Institution ==========

# Listar todos las EducationalInstitution
class EducationalInstitutionList(ListAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = EducationalInstitutionSerializer

# Listar un EducationalInstitution por id
class EducationalInstitutionDetail(RetrieveAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = EducationalInstitutionSerializer

# Crear un EducationalInstitution
class EducationalInstitutionCreate(ListCreateAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = CreateEducationalInstitutionSerializer

# Actualizar datos de un EducationalInstitution por id
class EducationalInstitutionUpdate(UpdateAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = UpdateEducationalInstitutionSerializer

# Eliminar EducationalInstitution
class EducationalInstitutionDelete(DestroyAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = DeleteEducationalInstitutionSerializer

# Inactvar EducationalInstitution
class EducationalInstitutionInactivate(UpdateAPIView):
    queryset = EducationalInstitution.objects.all()
    serializer_class = InactivateEducationalInstitutionSerializer

# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los Headquarters
class HeadquartersList(ListAPIView):
    queryset = Headquarters.objects.all()
    serializer_class = HeadquartersSerializer

# Listar un Headquarters
class HeadquartersDetail(RetrieveAPIView):
    queryset = Headquarters.objects.all()
    serializer_class = HeadquartersSerializer

# Crear cliente asignando un Headquarters ya existente
class HeadquartersCreate(ListCreateAPIView):
    queryset = Headquarters.objects.all()
    serializer_class = CreateHeadquartersSerializer

# Actualizar datos de Headquarters por id
class HeadquartersUpdate(UpdateAPIView):
    queryset = Headquarters.objects.all()
    serializer_class = UpdateHeadquartersSerializer

# Eliminar Un Headquarters sin afectar usuario
class HeadquartersDelete(DestroyAPIView):
    queryset = Headquarters.objects.all()
    serializer_class =  DeleteHeadquartersSerializer

# Inactvar Headquarters
class HeadquartersInactivate(UpdateAPIView):
    queryset = Headquarters.objects.all()
    serializer_class = InactivateHeadquartersSerializer