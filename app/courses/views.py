from .models import (
    Course,
    Area,
    AcademicCharge,
    TimeTable
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

from .serializers import (
    AreaSerializer,
    CreateAreaSerializer,
    UpdateAreaSerializer,
    DeleteAreaSerializer,
    
    CourseSerializer,
    CreateCourseSerializer,
    UpdateCourseSerializer,
    DeleteCourseSerializer,
    
    AcademicChargeSerializer,
    CreateAcademicChargeSerializer,
    UpdateAcademicChargeSerializer,
    DeleteAcademicChargeSerializer,
    
    TimeTableSerializer,
    CreateTimeTableSerializer,
    UpdateTimeTableSerializer,
    DeleteTimeTableSerializer
)

# ========== Area ===================================================================================


class AreaList(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

# Listar un Area por id

class AreaDetail(RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

# Crear Area asignando un usuario ya existente

class AreaCreate(ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = CreateAreaSerializer

# Actualizar datos de Area por id

class AreaUpdate(UpdateAPIView):
    queryset = Area.objects.all()
    serializer_class = UpdateAreaSerializer

# Eliminar Un Area sin afectar usuario

class AreaDelete(DestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
# ========== Courses ===================================================================================


class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Listar un Course por id


class CourseDetail(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Crear Course asignando un usuario ya existente


class CourseCreate(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer

# Actualizar datos de Course por id


class CourseUpdate(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = UpdateCourseSerializer

# Eliminar Un Course sin afectar usuario


class CourseDelete(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# ========== AcademicCharge ===================================================================================

class AcademicChargeList(ListAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = AcademicChargeSerializer

# Listar un AcademicCharge por id


class AcademicChargeDetail(RetrieveAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = AcademicChargeSerializer

# Crear AcademicCharge asignando un usuario ya existente


class AcademicChargeCreate(ListCreateAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = CreateAcademicChargeSerializer

# Actualizar datos de AcademicCharge por id


class AcademicChargeUpdate(UpdateAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = UpdateAcademicChargeSerializer

# Eliminar Un AcademicCharge sin afectar usuario


class AcademicChargeDelete(DestroyAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = AcademicChargeSerializer

# ========== TimeTable ===================================================================================

class TimeTableList(ListAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

# Listar un TimeTable por id


class TimeTableDetail(RetrieveAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

# Crear TimeTable asignando un usuario ya existente


class TimeTableCreate(ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = CreateTimeTableSerializer

# Actualizar datos de TimeTable por id


class TimeTableUpdate(UpdateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = UpdateTimeTableSerializer

# Eliminar Un TimeTable sin afectar usuario


class TimeTableDelete(DestroyAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
