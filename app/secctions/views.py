# Create your views here.

"""Serializers for the Resource"""
from .models import (
    Resource,
    Secction,
    HyperLynks,
    ResponseSecction,
    Comment,
    Homework,
    Responses,
)

from workspace.models import WorkSpace
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.parsers import FileUploadParser
from rest_framework import status

from .serializers import (
    # Resource
    ResourceSerializer,
    DeleteResourceSerializers,
    # Hyperlyncs
    HyperLynksSerializer,
    CreateHyperLynksSerializer,
    UpdateHyperLynksSerializer,
    DeleteHyperLynksSerializer,
    # Secction
    SecctionSerializer,
    CreateSecctionSerializer,
    UpdateSecctionSerializer,
    DeleteSecctionSerializer,
    # Respose Secction
    ResponseSecctionSerializer,
    UpdateResponseSecctionSerializer,
    DeleteResponseSecctionSerializer,
    ResponseSecctionbyAcademicchargeSerializer,
    # Responses
    ResponsesSerializer,
    CreateResponsesSerializer,
    ResponsesbyAcademicchargeSerializer,
    DeleteResponsesSerializer,
    UpdateResponsesSerializer,
    # Comment Response
    CommentSerializer,
    CreateCommentSerializer,
    DeleteCommentSerializer,
    UpdateCommentSerializer,
    # Homework
    HomeworkSerializer,
    DeleteHomeworkSerializers
)


# ========== upload to Resource ===================================================================================
class ResourceUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data Resource"""
        Resource_serializer = ResourceSerializer(data=request.data)
        if Resource_serializer.is_valid():
            """if the Resource is full then save"""
            Resource_serializer.save()
            return Response(Resource_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(Resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las Resource
class ResourceList(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# Listar un Resource por id


class ResourceDetail(RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

 # Delete un Resource por id


class ResourceDelete(DestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = DeleteResourceSerializers

# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los HyperLynks


class HyperLynksList(ListAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = HyperLynksSerializer

# Listar un HyperLynks


class HyperLynksDetail(RetrieveAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = HyperLynksSerializer

# Crear HyperLynks


class HyperLynksCreate(ListCreateAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = CreateHyperLynksSerializer

# Actualizar datos de HyperLynks por id


class HyperLynksUpdate(UpdateAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = UpdateHyperLynksSerializer

# Eliminar Un HyperLynks sin afectar usuario


class HyperLynksDelete(DestroyAPIView):
    queryset = HyperLynks.objects.all()
    serializer_class = DeleteHyperLynksSerializer

# ========== CRUD para la informacion del Transfomator ===================================

# Listar todos los Secction


class SecctionList(ListAPIView):
    queryset = Secction.objects.all()
    serializer_class = SecctionSerializer


class SecctionbyAcademicCharga(ListAPIView):
    queryset = Secction.objects.all()
    serializer_class = SecctionSerializer

    def get_queryset(self):
        workspace = WorkSpace.objects.get(
            academicCharge=self.kwargs['academicCharge'])
        code = workspace.codeWorkSpace
        query = Secction.objects.filter(
            workspaceSecction=code).order_by('-uploadOnSecction')
        return query


# Listar un Secction
class SecctionDetail(RetrieveAPIView):
    queryset = Secction.objects.all()
    serializer_class = SecctionSerializer

# Crear Secction


class SecctionCreate(ListCreateAPIView):
    queryset = Secction.objects.all()
    serializer_class = CreateSecctionSerializer

# Actualizar datos de Secction por id


class SecctionUpdate(UpdateAPIView):
    queryset = Secction.objects.all()
    serializer_class = UpdateSecctionSerializer

# Eliminar Un Secction sin afectar usuario


class SecctionDelete(DestroyAPIView):
    queryset = Secction.objects.all()
    serializer_class = DeleteSecctionSerializer

# ========== CRUD para la informacion del Response ===================================


class ResponseSecctionUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data Resource"""
        Response_serializer = ResponseSecctionSerializer(data=request.data)
        if Response_serializer.is_valid():
            """if the Resource is full then save"""
            Response_serializer.save()
            return Response(Response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(Response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las Resource
class ResponseSecctionList(ListAPIView):
    queryset = ResponseSecction.objects.all()
    serializer_class = ResponseSecctionSerializer

# Listar un Resource por id


class ResponseSecctionDetail(RetrieveAPIView):
    queryset = ResponseSecction.objects.all()
    serializer_class = ResponseSecctionSerializer


class ResponseSecctionStudentDetail(ListAPIView):
    queryset = ResponseSecction.objects.all()
    serializer_class = ResponseSecctionbyAcademicchargeSerializer

    def get_queryset(self):
        query = ResponseSecction.objects.get(secctionResponse=self.kwargs['secctionResponse'],
                                             studentResponse=self.kwargs['studentResponse'])
        return query

 # Delete un Resource por id


class ResponseSecctionDelete(DestroyAPIView):
    queryset = ResponseSecction.objects.all()
    serializer_class = DeleteResponseSecctionSerializer

# Actualizar datos de Secction por id


class ResponseSecctionUpdate(UpdateAPIView):
    queryset = ResponseSecction.objects.all()
    serializer_class = UpdateResponseSecctionSerializer
    parser_classes = (MultiPartParser, FormParser)

# ========== CRUD para la informacion del Comment ===================================


# Listar todos los Secction
class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Listar un Secction


class CommentDetail(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Crear Secction


class CommentCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer

# Actualizar datos de Secction por id


class CommentUpdate(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateCommentSerializer

# Eliminar Un Secction sin afectar usuario


class CommentDelete(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = DeleteCommentSerializer

######################
# ========== upload to Resource ===================================================================================


class HomeworkUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data Resource"""
        Homework_serializer = HomeworkSerializer(data=request.data)
        if Homework_serializer.is_valid():
            """if the Resource is full then save"""
            Homework_serializer.save()
            return Response(Homework_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(Homework_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las Resource
class HomeworkList(ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

# Listar un Resource por id


class HomeworkDetail(RetrieveAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

 # Delete un Resource por id


class HomeworkDelete(DestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = DeleteHomeworkSerializers


# ========== CRUD para la informacion del Response ===================================


# Listar todos las Resource
class ResponsesList(ListAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

# Listar un Resource por id


class ResponsesDetail(RetrieveAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer


class ResponsesStudentDetail(ListAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesbyAcademicchargeSerializer

    def get_queryset(self):
        query = Responses.objects.get(secction_response=self.kwargs['secction_response'],
                                      student_response=self.kwargs['student_response'])
        return query


class ResponsesCreate(ListCreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = CreateResponsesSerializer

 # Delete un Resource por id


class ResponsesDelete(DestroyAPIView):
    queryset = Responses.objects.all()
    serializer_class = DeleteResponsesSerializer

# Actualizar datos de Secction por id


class ResponsesUpdate(UpdateAPIView):
    queryset = Responses.objects.all()
    serializer_class = UpdateResponsesSerializer
