from .models import Enrollment
from groups.models import Group, Journey
from users.models import StudentUser
import json

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

from .serializers import (
    
    EnrollmentSerializer,
    CreateEnrollmentSerializer,
    UpdateEnrollmentSerializer,
    DeleteEnrollmentSerializer
)

# Create your views here.

# ========== Enrollment ===================================================================================

class EnrollmentList(ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Listar un Enrollment por id


class EnrollmentDetail(RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Crear Enrollment asignando un usuario ya existente

class EnrollmentCreate(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = CreateEnrollmentSerializer

class EnrollmentCreateMultiple(APIView):
    queryset = Enrollment.objects.all()

    def post(self, request):
        data = request.data
        for enrollment in data:
            print(enrollment)
            journey = enrollment.pop('journeyEnrollment')
            group = enrollment.pop('groupEnrollment')
            student = enrollment.pop('studentEnrollment')
            journeyObj = Journey.objects.get(codeJourney=journey)
            groupObj = Group.objects.get(nameGroup=group)
            studentObje = StudentUser.objects.get(codeStudent=student)
            enrollment = Enrollment.objects.create(journeyEnrollment=journeyObj,
                                                 groupEnrollment=groupObj,
                                                 studentEnrollment=studentObje,
                                                   **enrollment)
        return Response({"message": "Creacion exitoso",  "code": 200})



# Actualizar datos de Enrollment por id


class EnrollmentUpdate(UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = UpdateEnrollmentSerializer

# Eliminar Un Enrollment sin afectar usuario


class EnrollmentDelete(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer