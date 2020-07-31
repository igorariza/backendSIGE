from .models import Community, Addfile, Replay
# libreria serializers
from rest_framework import serializers
from users.models import CustomUser
from users.serializers import UserSerializer


class ReplaySerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Replay
        fields = ['codereplay', 'user', 'comment', 'datereplay', 'replay']


# ========== Serializador para crear la Replay ==========
class CreateReplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay
        fields = '__all__'

    def create(self, validated_data):
        replay = Replay.objects.create(
            user=validated_data['user'],
            comment=validated_data['comment'],
            replay=validated_data['replay']
        )
        replay.save()
        return replay

# ========== Serializador para actualizar la Replay ==========


class UpdateReplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay
        fields = ['comment']

    def update(self, instance, validated_data):
        replay = super().update(instance, validated_data)
        return replay

# ========== Serializador para eliminar la Replay ==========


class DeleteReplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


class AddfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addfile
        fields = ['codefile', 'post', 'file']

# ========== Serializador para eliminar la Addfile ==========


class DeleteAddfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = Addfile
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para una Community =================================================================
class CommunitySerializer(serializers.ModelSerializer):

    user = UserSerializer()
    replays = ReplaySerializer(many=True, read_only=True)
    file = AddfileSerializer(read_only=True)


    class Meta:
        model = Community
        fields = ['codeCommunity', 'titleCommunity', 'descriptionCommunity',
                  'user', 'dateCommunity', 'replays', 'file']


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
