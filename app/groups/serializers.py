from .models import Group, Journey
from users.models import StudentUser

# libreria serializers
from rest_framework import serializers
from users.serializers import TeacherSerializer


# ========== Serializador para un Grupo =================================================================
class GroupSerializer(serializers.ModelSerializer):

   # managerGroup = TeacherSerializer()

    class Meta:
        model = Group
        fields = [
            'nameGroup',
            'journeyGroup',
            'headquarter',
            'managerGroup']

# ========== Serializador para crear el grupo ==========


class CreateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        group = Group.objects.create(
            nameGroup=validated_data['nameGroup'],
            journeyGroup=validated_data['journeyGroup'],
            managerGroup=validated_data['managerGroup'],
            headquarter=validated_data['headquarter']
        )
        group.save()
        return group

# ========== Serializador para actualizar la IE ==========


class UpdateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = [
            'journeyGroup',
            'managerGroup',
            'headquarter']

    def update(self, instance, validated_data):
        group = super().update(instance, validated_data)
        return group

# ========== Serializador para eliminar la IE ==========


class DeleteGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para un Journey =================================================================
class JourneySerializer(serializers.ModelSerializer):

    #groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = Journey
        fields = ['codeJourney','nameJourney']

# ========== Serializador para crear el grupo ==========


class CreateJourneyerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = '__all__'

    def create(self, validated_data):
        journey = Journey.objects.create(
            nameJourney=validated_data['nameJourney'])
        journey.save()
        return journey

# ========== Serializador para actualizar la IE ==========


class UpdateJourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = ['nameJourney']

    def update(self, instance, validated_data):
        journey = super().update(instance, validated_data)
        return journey

# ========== Serializador para eliminar la IE ==========
class DeleteJourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()
