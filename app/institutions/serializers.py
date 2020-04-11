from rest_framework import serializers
from .models import EducationalInstitution, Headquarters


# ========== Serializador para una IE =================================================================
class EducationalInstitutionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EducationalInstitution
        fields = ['codeIE', 'nameIE', 'nitIE', 'is_active']

# ========== Serializador para crear la IE ==========
class CreateEducationalInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalInstitution
        fields = ['codeIE', 'nameIE', 'nitIE', 'is_active']

    def create(self, validated_data):
        ie = EducationalInstitution.objects.create(
            nameIE=validated_data['nameIE'],
            nitIE=validated_data['nitIE'],
            is_active=validated_data['is_active']
        )
        ie.save()
        return ie

# ========== Serializador para actualizar la IE ==========
class UpdateEducationalInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalInstitution
        fields = ['codeIE', 'nameIE', 'nitIE', 'is_active']

    def update(self, instance, validated_data):
        ie = super().update(instance, validated_data)
        return ie

# ========== Serializador para inactivar la IE ==========
class InactivateEducationalInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalInstitution
        fields = ['codeIE', 'nameIE', 'nitIE', 'is_active']

    def patch(self, request, *args, **kwargs):
        ie = self.partial_update(request, *args, **kwargs)
        return ie
    
# ========== Serializador para eliminar la IE ==========
class DeleteEducationalInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalInstitution
        fields = ['codeIE', 'nameIE', 'nitIE', 'is_active']

    def perform_destroy(self, instance):
            instance.delete()
 
# ========== Serializador para el Transformator =====================================================
class HeadquartersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headquarters
        fields = ['codeHeadquarters', 'nameHeadquarters', 'daneHeadquarters', 'codeIE', 'is_active']

# ========== Serializador para crear una headquarters ==========
class CreateHeadquartersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headquarters
        fields = ['codeHeadquarters', 'nameHeadquarters', 'daneHeadquarters', 'codeIE', 'is_active']

    def create(self, validated_data):
        headquarters = Headquarters.objects.create(
            nameHeadquarters=validated_data['nameHeadquarters'],
            daneHeadquarters=validated_data['daneHeadquarters'],
            codeIE=validated_data['codeIE'],
            is_active=validated_data['is_active']
            )
        headquarters.save()
        return headquarters

# ========== Serializador para actualizar una headquarters ==========
class UpdateHeadquartersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headquarters
        fields = ['codeHeadquarters', 'nameHeadquarters', 'daneHeadquarters', 'codeIE', 'is_active']

    def update(self, instance, validated_data):
        headquarters = super().update(instance, validated_data)
        return headquarters

# ========== Serializador para inactivar una headquarters ==========
class InactivateHeadquartersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headquarters
        fields = ['codeHeadquarters', 'nameHeadquarters', 'daneHeadquarters', 'codeIE', 'is_active']

    def patch(self, request, *args, **kwargs):
        headquarters = self.partial_update(request, *args, **kwargs)
        return headquarters
    
    
 # ========== Serializador para actualizar una headquarters ==========
class DeleteHeadquartersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headquarters
        fields = ['codeHeadquarters', 'nameHeadquarters', 'daneHeadquarters', 'codeIE', 'is_active']

    def perform_destroy(self, instance):
            instance.delete()
    