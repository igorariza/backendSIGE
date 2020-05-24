from .models import (Secction,
                     Resource,
                     HyperLynks
                     )
# libreria serializers
from rest_framework import serializers


# ========== Serializador para una Resource =================================================================
class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['codeResouce','resource','secctionResource']

# ========== Serializador para eliminar la Resource ==========


class DeleteResourceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para un URL =================================================================
class HyperLynksSerializer(serializers.ModelSerializer):

    class Meta:
        model = HyperLynks
        fields = '__all__'

# ========== Serializador para crear el URL ==========


class CreateHyperLynksSerializer(serializers.ModelSerializer):

    class Meta:
        model = HyperLynks
        fields = [
            'url',
            'secctionHyperlink'
        ]

    def create(self, validated_data):
        hyperlynk = HyperLynks.objects.create(
            url=validated_data['url'],
            secctionHyperlink=validated_data['secctionHyperlink']
        )
        hyperlynk.save()
        return hyperlynk

# ========== Serializador para actualizar la IE ==========


class UpdateHyperLynksSerializer(serializers.ModelSerializer):

    class Meta:
        model = HyperLynks
        fields = '__all__'

    def update(self, instance, validated_data):
        hyperlynk = super().update(instance, validated_data)
        return hyperlynk

# ========== Serializador para eliminar la IE ==========


class DeleteHyperLynksSerializer(serializers.ModelSerializer):

    class Meta:
        model = HyperLynks
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para un SecctionSerializer =================================================================
class SecctionSerializer(serializers.ModelSerializer):

    resources = ResourceSerializer(many=True, read_only=True)
    lynks = HyperLynksSerializer(many=True, read_only=True)

    class Meta:
        model = Secction
        fields = ['codeSecction',
                  'nameSecction',
                  'descriptionSecction',
                  'uploadOnSecction',
                  'workspaceSecction',
                  'resources',
                  'lynks']

# ========== Serializador para crear el SecctionSerializer ==========


class CreateSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secction
        fields = '__all__'

    def create(self, validated_data):
          secction = Secction.objects.create(
                nameSecction=validated_data['nameSecction'],
                descriptionSecction=validated_data['descriptionSecction'],
                workspaceSecction=validated_data['workspaceSecction']
            )
          secction.save()
          return secction

# ========== Serializador para actualizar la IE ==========


class UpdateSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secction
        fields = ['nameSecction',
                  'workspaceSecction',
                  'descriptionSecction']

    def update(self, instance, validated_data):
        Secction = super().update(instance, validated_data)
        return Secction

# ========== Serializador para eliminar la IE ==========


class DeleteSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secction
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()
