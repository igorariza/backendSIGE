from .models import Feed, File_forum, Replay_feed_forum
# libreria serializers
from rest_framework import serializers
from users.models import CustomUser
from users.serializers import UserSerializer


class Replay_feed_forumSerializer(serializers.ModelSerializer):

    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Replay_feed_forum
        fields = ['code_replay_feed', 'user_id',
                  'comment', 'dateComment', 'replay_feed']


# ========== Serializador para crear la Replay ==========
class CreateReplay_feed_forumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay_feed_forum
        fields = '__all__'


    def create(self, validated_data):
        replay = Replay_feed_forum.objects.create(
            user_id=validated_data['user_id'],
            comment=validated_data['comment'],
            replay_feed=validated_data['replay_feed'],
        )
        replay.save()
        return replay

# ========== Serializador para actualizar la Replay ==========


class UpdateReplay_feed_forumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay_feed_forum
        fields = ['comment']

    def update(self, instance, validated_data):
        replay = super().update(instance, validated_data)
        return replay

# ========== Serializador para eliminar la Replay ==========


class DeleteReplay_feed_forumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay_feed_forum
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


class File_forumSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_forum
        fields = ['code_file', 'feed_id', 'resource']

# ========== Serializador para eliminar la Addfile ==========


class DeleteFile_forumSerializers(serializers.ModelSerializer):

    class Meta:
        model = File_forum
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete() 


# ========== Serializador para una Feed =================================================================
class FeedSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    replays = Replay_feed_forumSerializer(many=True, read_only=True)
    infos = File_forumSerializer(read_only=True,many=True)

    class Meta:
        model = Feed
        fields = ['code_feed', 'title_feed', 'description_feed',
                  'user', 'date_feed', 'academic_charge', 'replays', 'infos']


# ========== Serializador para crear la Feed ==========
class CreateFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model= Feed
        fields= '__all__'

    def create(self, validated_data):
        feed= Feed.objects.create(
            title_feed=validated_data['title_feed'],
            description_feed=validated_data['description_feed'],
            user=validated_data['user'],
            academic_charge=validated_data['academic_charge']
        )
        feed.save()
        return feed

# ========== Serializador para actualizar la Feed ==========


class UpdateFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model= Feed
        fields= ['title_feed', 'description_feed']

    def update(self, instance, validated_data):
        feed= super().update(instance, validated_data)
        return feed

# ========== Serializador para eliminar la Feed ==========


class DeleteFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model= Feed
        fields= "__all__"

    def perform_destroy(self, instance):
        instance.delete()
