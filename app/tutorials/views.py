
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
    )

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tutorials

from .serializers import (
    TutorialsSerializer,
    CreateTutorialsSerializer,
    DeleteTutorialsSerializer,
    UpdateTutorialsSerializer
    )

# ========== Tutorials ===================================================================================

class TutorialsList(ListAPIView):
    queryset = Tutorials.objects.all()
    serializer_class = TutorialsSerializer

# Listar un Tutorials por id


class TutorialsDetail(RetrieveAPIView):
    queryset = Tutorials.objects.all()
    serializer_class = TutorialsSerializer

# Crear Tutorials asignando un usuario ya existente


class TutorialsCreate(ListCreateAPIView):
    queryset = Tutorials.objects.all()
    serializer_class = CreateTutorialsSerializer


class TutorialsCreateMultiple(APIView):
    queryset = Tutorials.objects.all()

    def post(self, request):
        data = request.data
        for Tutorials in data:
            Tutorials = Tutorials.objects.create(**Tutorials)
        return Response({"message": "Creacion exitoso",  "code": 200})

# Actualizar datos de Tutorials por id


class TutorialsUpdate(UpdateAPIView):
    queryset = Tutorials.objects.all()
    serializer_class = UpdateTutorialsSerializer

# Eliminar Un Tutorials sin afectar usuario


class TutorialsDelete(DestroyAPIView):
    queryset = Tutorials.objects.all()
    serializer_class = TutorialsSerializer
