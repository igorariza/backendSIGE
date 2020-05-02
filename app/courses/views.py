from .models import (
    Course,
    Area,
    AcademicCharge,
    TimeTable
)
from groups.models import Group
from users.models import TeacherUser
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
    AcademicChargeGetGroupsSerializer,

    TimeTableSerializer,
    CreateTimeTableSerializer,
    UpdateTimeTableSerializer,
    DeleteTimeTableSerializer
)

from django.db.models import Count

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
    
class AreaCreateMultiple(APIView):
    queryset = Area.objects.all()

    def post(self, request):
        data = request.data
        for area in data:
            area = Area.objects.create(**area)
        return Response({"message": "Creacion exitoso",  "code": 200})

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


class CourseCreateMultiple(APIView):
    queryset = Course.objects.all()

    def post(self, request):
        data = request.data
        for course in data:
            print(course)
            areacode = course.pop('areaCourse')
            area = Area.objects.get(codeArea=areacode)
            materia = Course.objects.create(areaCourse=area, **course)
        return Response({"message": "Creacion exitoso",  "code": 200})


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

class AcademicChargeCoursesListTeacher(ListAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = AcademicChargeGetGroupsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `teacherDictate` query parameter in the URL.
        """
        #teacher = self.kwargs['teacherDictate']
        charga = AcademicCharge.objects.raw('SELECT  "groupDictate_id" FROM "courses_academiccharge" WHERE "teacherDictate_id"={}  GROUP BY "groupDictate_id"'.format(
            self.kwargs['teacherDictate']))
        
        #filter(teacherDictate=teacher).order_by('groupDictate__nameGroup')
        #filterdata = charga.filter(teacherDictate=teacher)
        return charga


# Listar un AcademicCharge por id


class AcademicChargeDetail(RetrieveAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = AcademicChargeSerializer

# Crear AcademicCharge asignando un usuario ya existente


class AcademicChargeCreate(ListCreateAPIView):
    queryset = AcademicCharge.objects.all()
    serializer_class = CreateAcademicChargeSerializer

class AcademicChargeCreateMultiple(APIView):
    queryset = AcademicCharge.objects.all()

    def post(self, request):
        data = request.data
        for workspace in data:
            print(workspace)
            cuours = workspace.pop('courseDictate')
            group = workspace.pop('groupDictate')
            teacher = workspace.pop('teacherDictate')
            courseObj = Course.objects.get(codeCourse=cuours)
            groupObj = Group.objects.get(nameGroup=group)
            teacherObje = TeacherUser.objects.get(codeTeacher=teacher)
            workSpace = AcademicCharge.objects.create(courseDictate=courseObj,
                                                 groupDictate=groupObj,
                                                 teacherDictate=teacherObje,
                                                   **workspace)
        return Response({"message": "Creacion exitoso",  "code": 200})



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
