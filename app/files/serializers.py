from .models import (File,
                          Evidence
                        )
#libreria serializers
from rest_framework import serializers


 
# ========== Serializador para una File =================================================================
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
    
# ========== Serializador para eliminar la File ==========
class DeleteFileSerializers(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = "__all__"

    def perform_destroy(self, instance):
            instance.delete()         
            
# ========== Serializador para una Evidence =================================================================
class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ['codeEvidence', 'nameEvidence', 'descriptionEvidence',
                  'teacher', 'typeEvidence', 'file']

        
# ========== Serializador para crear la Evidence ==========
class CreateEvidenceSerializer(serializers.ModelSerializer):

    file = FileSerializer()

    class Meta:
        model = Evidence
        fields = ['codeEvidence', 'nameEvidence', 'descriptionEvidence',
                  'teacher', 'typeEvidence', 'file']
        

    def create(self, validated_data):
            file = validated_data.pop('file')
            files = File.objects.create(**file)
            evidence = Evidence.objects.create(file=files, **validated_data)
            return evidence

# ========== Serializador para actualizar la Evidence ==========
class UpdateEvidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evidence
        fields = "__all__"

    def update(self, instance, validated_data):
        evidence = super().update(instance, validated_data)
        return evidence

# ========== Serializador para eliminar la Evidence ==========
class DeleteEvidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evidence
        fields = "__all__"

    def perform_destroy(self, instance):
            instance.delete()


# ========== Serializador para una ProfilePicture =================================================================