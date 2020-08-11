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
from django.db.models import Prefetch
from courses.models import AcademicCharge

from .serializers import (
    WorkSpaceSerializer,
    WorkSpaceSerializerCustom,
    CreateWorkSpaceSerializer,
    UpdateWorkSpaceSerializer,
    DeleteWorkSpaceSerializer,
    WorkSpaceOnlySecctionsSerializer,
    WorkSpaceStudentSerializer,
)

from rest_framework import viewsets
from django.db.models import Prefetch

from rest_framework.views import APIView
from rest_framework.response import Response


# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los WorkSpace
class WorkSpaceList(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer

# Trae el espacacio de trabajo para un curso y su maestro


class WorkSpaceCoursesTeacher(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `teacherDictate` query parameter in the URL.
        """
        teacher = self.kwargs['teacherDictate']
        group = self.kwargs['groupDictate']
        charga = WorkSpace.objects.all()
        return charga.filter(
            academicCharge__teacherDictate=teacher, academicCharge__groupDictate=group)


class WorkSpaceByAcademicCharge(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializerCustom

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `teacherDictate` query parameter in the URL.
        """
        code_academic_charge = self.kwargs['codeAcademicCharge']
        charga = WorkSpace.objects.all()
        return charga.filter(
            academicCharge=code_academic_charge
        )


# Listar un WorkSpace


class WorkSpaceDetail(RetrieveAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer


class WorkSpaceDetailCourse(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer

    def get_queryset(self):
        charga = WorkSpace.objects.all().filter(
            academicCharge=self.kwargs['academicCharge'])
        return charga


class WorkSpaceDetailStudentCourse(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceStudentSerializer

    def get_queryset(self):
        charga = WorkSpace.objects.all().filter(
            academicCharge=self.kwargs['academicCharge'])
        return charga

# Crear WorkSpace


class WorkSpaceCreate(ListCreateAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = CreateWorkSpaceSerializer


class WorkSpaceCreateMultiple(APIView):
    queryset = WorkSpace.objects.all()

    def post(self, request):
        data = request.data
        for workspace in data:
            print(workspace)
            charga = workspace.pop('academicCharge')
            chargaObj = AcademicCharge.objects.get(codeAcademicCharge=charga)
            workSpace = WorkSpace.objects.create(academicCharge=chargaObj,
                                                 **workspace)
        return Response({"message": "Creacion exitoso",  "code": 200})


# Actualizar datos de WorkSpace por id


class WorkSpaceUpdate(UpdateAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = UpdateWorkSpaceSerializer

# Eliminar Un WorkSpace sin afectar usuario


class WorkSpaceDelete(DestroyAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = DeleteWorkSpaceSerializer


class WorkSpaceOnlySecctions(ListAPIView):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceOnlySecctionsSerializer

    def get_queryset(self):
        charga = WorkSpace.objects.all().filter(
            academicCharge__teacherDictate=self.kwargs['teacherDictate'])
        return charga
