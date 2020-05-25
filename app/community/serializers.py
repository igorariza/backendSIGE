from .models import Community
#libreria serializers
from rest_framework import serializers
from users.models import CustomUser
from users.serializers import UserSerializer


             
# ========== Serializador para una Community =================================================================
class CommunitySerializer(serializers.ModelSerializer):
   
    user = UserSerializer()
    class Meta:
        model = Community
        fields = ['codeCommunity', 'titleCommunity', 'descriptionCommunity',
                  'user', 'dateCommunity']

        
# ========== Serializador para crear la Community ==========
class CreateCommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ['titleCommunity', 'descriptionCommunity',
                  'user']
        
    def create(self, validated_data):
            community = Community.objects.create(
                    titleCommunity=validated_data['titleCommunity'],
                    descriptionCommunity=validated_data['descriptionCommunity'],
                    user=validated_data['user']
                )
            community.save()
            return community

# ========== Serializador para actualizar la Community ==========
class UpdateCommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = "__all__"

    def update(self, instance, validated_data):
        Community = super().update(instance, validated_data)
        return Community

# ========== Serializador para eliminar la Community ==========
class DeleteCommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = "__all__"

    def perform_destroy(self, instance):
            instance.delete()


# ========== Serializador para una ProfilePicture