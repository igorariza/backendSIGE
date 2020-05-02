from .models import Enrollment

from groups.serializers import GroupSerializer, JourneySerializer
from users.serializers import StudentSerializer
# libreria serializers
from rest_framework import serializers

# ========== Serializador para la Matricula =================================================================


class EnrollmentSerializer(serializers.ModelSerializer):

    groupEnrollment = GroupSerializer()
    journeyEnrollment = JourneySerializer()
    studentEnrollment = StudentSerializer()

    class Meta:
        model = Enrollment
        fields = [
            'codeEnrollment',
            'groupEnrollment',
            'journeyEnrollment',
            'studentEnrollment',
            'dateEnrollment',
            'is_active'
            ]


# ========== Serializador para crear la Matricula ==========
class CreateEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = [
            'codeEnrollment',
            'groupEnrollment',
            'journeyEnrollment',
            'studentEnrollment',
            'dateEnrollment',
            'is_active'
            ]

    def create(self, validated_data):
        enrollment = Enrollment.objects.create(
            groupEnrollment=validated_data['groupEnrollment'],
            journeyEnrollment=validated_data['journeyEnrollment'],
            studentEnrollment=validated_data['studentEnrollment'],
            is_active=validated_data['is_active']
        )
        enrollment.save()
        return enrollment

# ========== Serializador para actualizar la Matricula ==========


class UpdateEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = "__all__"

    def update(self, instance, validated_data):
        enrollment = super().update(instance, validated_data)
        return enrollment

# ========== Serializador para eliminar la Matricula ==========


class DeleteEnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()
