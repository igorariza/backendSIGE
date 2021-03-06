# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Group, Journey
from users.models import TeacherUser
from institutions.models import Headquarters

from .serializers import (
    GroupSerializer,
    CreateGroupSerializer,
    UpdateGroupSerializer,
    DeleteGroupSerializer,
    
    JourneySerializer,
    CreateJourneyerializer,
    UpdateJourneySerializer,
    DeleteJourneySerializer
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

# Crear Journey 
class JourneyCreate(ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = CreateJourneyerializer

# Actualizar datos de Journey por id
class JourneyUpdate(UpdateAPIView):
    queryset = Journey.objects.all()
    serializer_class = UpdateJourneySerializer

# Eliminar Un Journey sin afectar usuario
class JourneyDelete(DestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class =  DeleteJourneySerializer

class JourneyList(ListAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

# Listar un Journey
class JourneyDetail(RetrieveAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

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
    
    
class GroupCreateMultiple(APIView):
    queryset = Group.objects.all()

    def post(self, request):
        data = request.data
        for group in data:
            print(Group)
            jouneycode = group.pop('journeyGroup')
            teachercode = group.pop('managerGroup')
            headqcode = group.pop('headquarter')
            jounreyObj = Journey.objects.get(codeJourney=jouneycode)
            managerObj = TeacherUser.objects.get(codeTeacher=teachercode)
            headObj = Headquarters.objects.get(codeHeadquarters=headqcode)
            
            materia = Group.objects.create(journeyGroup=jounreyObj,
                                           managerGroup=managerObj,
                                           headquarter=headObj,
                                            **group)
        return Response({"message": "Creacion exitoso",  "code": 200})
