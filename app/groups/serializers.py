from .models import Group
from users.models import StudentUser

#libreria serializers
from rest_framework import serializers
from users.serializers import TeacherSerializer


# ========== Serializador para un Grupo =================================================================
class GroupSerializer(serializers.ModelSerializer):
    
    managerGroup = TeacherSerializer()
    class Meta:
        model = Group
        fields = ['schoolyear',
                  'nameGroup',
                  'workingDay',
                  'headquarter',
                  'managerGroup']

# ========== Serializador para crear el grupo ==========
class CreateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        group = Group.objects.create(
            schoolyear=validated_data['schoolyear'],
            nameGroup=validated_data['nameGroup'],
            workingDay=validated_data['workingDay'],
            managerGroup=validated_data['managerGroup'],
            headquarter=validated_data['headquarter']
        )
        group.save()
        return group

# ========== Serializador para actualizar la IE ==========
class UpdateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['nameGroup',
                  'workingDay',
                  'managerGroup']

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
 