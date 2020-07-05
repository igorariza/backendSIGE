
"""Serializers for the ProfilePicture"""
from .models import ProfilePicture

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
    # Picture
    ProfilePictureSerializer,
    DeleteProfilePictureSerializers
)


# ========== upload to ProfilePicture ===================================================================================
class ProfilePictureUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """keept the data ProfilePicture"""
        ProfilePicture_serializer = ProfilePictureSerializer(data=request.data)
        if ProfilePicture_serializer.is_valid():
            """if the ProfilePicture is full then save"""
            ProfilePicture_serializer.save()
            return Response(ProfilePicture_serializer.data, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response(ProfilePicture_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar todos las ProfilePicture
class ProfilePictureList(ListAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer

# Listar un ProfilePicture por id


class ProfilePictureDetail(RetrieveAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer

 # Delete un ProfilePicture por id


class ProfilePictureByUser(APIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer

    """Consegir las materias que ve un alumno por su grupo"""

    def post(self, request):
        user = request.data.get('user', None)
        profilePicture = ProfilePicture.objects.filter(
            user=user).values(
                'codePhoto',
                'photo',
                'user'
        )
        if profilePicture.exists():
            pic = profilePicture[0]
            return Response(pic, status=status.HTTP_201_CREATED)
        else:
            """return a bad request code"""
            return Response({"picture": ""}, status=status.HTTP_400_BAD_REQUEST)


class ProfilePictureDelete(DestroyAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = DeleteProfilePictureSerializers
