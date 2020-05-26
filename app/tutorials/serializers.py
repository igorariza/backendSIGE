from .models import Tutorials

# libreria serializers
from rest_framework import serializers


class TutorialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorials
        fields = '__all__'


class CreateTutorialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorials
        fields = [
            'nameTutorial',
            'typeTutorial',
            'urlTutorial',
            'likeTutorial'
            ]

    def create(self, validated_data):
        tutorials = Tutorials.objects.create(
            nameTutorials=validated_data['nameTutorials'],
            typeTutorial=validated_data['typeTutorial'],
            urlTutorial=validated_data['nameTutorials'],
            likeTutorial=validated_data['likeTutorial']
        )
        tutorials.save()
        return tutorials


class UpdateTutorialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorials
        fields = [
            'nameTutorial',
            'typeTutorial',
            'urlTutorial',
            'likeTutorial'
            ]

    def update(self, instance, validated_data):
        tutorials = super().update(instance, validated_data)
        return tutorials


class DeleteTutorialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorials
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()
