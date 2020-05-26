from .models import ProfilePicture
                     
# libreria serializers
from rest_framework import serializers



# ========== Serializador para una ProfilePicture =================================================================
class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'

# ========== Serializador para eliminar la ProfilePicture ==========


class DeleteProfilePictureSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProfilePicture
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()
