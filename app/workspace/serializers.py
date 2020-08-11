# modelos
from .models import WorkSpace

# libreria serializers
from rest_framework import serializers
from courses.serializers import AcademicChargeSerializer
from secctions.serializers import SecctionSerializer,SecctionStudentSerializer


# ========== Serializador para un Grupo =================================================================
class WorkSpaceSerializer(serializers.ModelSerializer):

    academicCharge = AcademicChargeSerializer()
    secctions = SecctionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkSpace
        fields = ['codeWorkSpace',
                  'nameWorkSpace',
                  'descriptionWorkSpace',
                  'academicCharge',
                  'secctions'
                  ]

                  
class WorkSpaceSerializerCustom(serializers.ModelSerializer):

    academicCharge = AcademicChargeSerializer()

    class Meta:
        model = WorkSpace
        fields = ['codeWorkSpace',
                  'nameWorkSpace',
                  'descriptionWorkSpace',
                  'academicCharge'
                  ]


class WorkSpaceStudentSerializer(serializers.ModelSerializer):
    
    academicCharge = AcademicChargeSerializer()
    secctions = SecctionStudentSerializer(many=True, read_only=True)

    class Meta:
        model = WorkSpace
        fields = ['codeWorkSpace',
                  'nameWorkSpace',
                  'descriptionWorkSpace',
                  'academicCharge',
                  'secctions'
                  ]

class WorkSpaceOnlySecctionsSerializer(serializers.ModelSerializer):
    
    #academicCharge = AcademicChargeSerializer()
    secctions = SecctionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkSpace
        fields = [
                  'secctions'
                  ]


# ========== Serializador para crear el grupo ==========

class CreateWorkSpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSpace
        fields = [
                  'nameWorkSpace',
                  'descriptionWorkSpace',
                  'academicCharge'  
                  ]

    def create(self, validated_data):
        workspace = WorkSpace.objects.create(
            nameWorkSpace=validated_data['nameWorkSpace'],
            academicCharge=validated_data['academicCharge'],
            descriptionWorkSpace=validated_data['descriptionWorkSpace']
            )
        workspace.save()
        return workspace

# ========== Serializador para actualizar la IE ==========


class UpdateWorkSpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSpace
        fields = ['nameWorkSpace',
                  'workingDay',
                  'managerWorkSpace']

    def update(self, instance, validated_data):
        workspace = super().update(instance, validated_data)
        return workspace

# ========== Serializador para eliminar la IE ==========


class DeleteWorkSpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSpace
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()

