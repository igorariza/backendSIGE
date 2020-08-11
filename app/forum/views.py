# Create your views here.

"""Serializers for the File"""
from .models import Feed, File_forum, Replay_feed_forum

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
from rest_framework import status
from .serializers import (
    # Feed
    FeedSerializer,
    CreateFeedSerializer,
    UpdateFeedSerializer,
    DeleteFeedSerializer,
    # File_forum
    File_forumSerializer,
    DeleteFile_forumSerializers,
    # R
    CreateReplay_feed_forumSerializer,
    UpdateReplay_feed_forumSerializer,
    DeleteReplay_feed_forumSerializer,
    Replay_feed_forumSerializer,
)

# ========== Feed ===================================================================================


# Listar todos los Secction
class Replay_feed_forumList(ListAPIView):
    queryset = Replay_feed_forum.objects.all()
    serializer_class = Replay_feed_forumSerializer

# Listar un Secction
class Replay_feed_forumDetail(RetrieveAPIView):
    queryset = Replay_feed_forum.objects.all()
    serializer_class = Replay_feed_forumSerializer

# Crear Secction
class Replay_feed_forumCreate(ListCreateAPIView):
    queryset = Replay_feed_forum.objects.all()
    serializer_class = CreateReplay_feed_forumSerializer

# Actualizar datos de Secction por id
class Replay_feed_forumUpdate(UpdateAPIView):
    queryset = Replay_feed_forum.objects.all()
    serializer_class = UpdateReplay_feed_forumSerializer

# Eliminar Un Secction sin afectar usuario


class Replay_feed_forumDelete(DestroyAPIView):
    queryset = Replay_feed_forum.objects.all()
    serializer_eplaReplay_feed_forumclass = DeleteReplay_feed_forumSerializer


class File_forumUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data File_forum"""
        File_forum_serializer = File_forumSerializer(data=request.data)
        if File_forum_serializer.is_valid():
            """if the File_forum is full then save"""
            File_forum_serializer.save()
            return Response(File_forum_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(File_forum_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las File_forum
class File_forumList(ListAPIView):
    queryset = File_forum.objects.all()
    serializer_class = File_forumSerializer

# Listar un File_forum por id


class File_forumDetail(RetrieveAPIView):
    queryset = File_forum.objects.all()
    serializer_class = File_forumSerializer

 # Delete un File_forum por id


class File_forumDelete(DestroyAPIView):
    queryset = File_forum.objects.all()
    serializer_class = DeleteFile_forumSerializers


class FeedList(ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

# Listar un Feed por id


class FeedDetail(RetrieveAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

# Crear Feed asignando un usuario ya existente


class FeedCreate(ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = CreateFeedSerializer


class FeedgetbyAcadmicCharga(ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = CreateFeedSerializer

    def get_queryset(self):
        query = Feed.objects.all().filter(
            academic_charge=self.kwargs['academic_charge'])
        return query
    

# Actualizar datos de Feed por id


class FeedUpdate(UpdateAPIView):
    queryset = Feed.objects.all()
    serializer_class = UpdateFeedSerializer

# Eliminar Un Feed sin afectar usuario


class FeedDelete(DestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


# ========== upload to ProfilePicture ===================================================================================
class FeedListbyIE(ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get_queryset(self):
        Feeds = Feed.objects.all().filter(
            user__codeIE=self.kwargs['codeIE'])
        return Feeds

class FeedListbyAcademicCharge(ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get_queryset(self):
        Feeds = Feed.objects.all().filter(
            academic_charge=self.kwargs['codeAcademicCharge'])
        return Feeds
