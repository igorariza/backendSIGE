from .models import *
# libreria serializers
from rest_framework import serializers
from users.models import CustomUser
from users.serializers import UserSerializer


class AttendanceSerializer(serializers.ModelSerializer):

    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ['attendance_date', 'attendance',
                  'forum_feed_id', 'user_id']


# ========== Serializador para crear la Replay ==========
class CreateAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'


    def create(self, validated_data):
        attendance = Attendance.objects.create(
            attendance=validated_data['attendance'],
            forum_feed_id=validated_data['forum_feed_id'],
            user_id=validated_data['user_id']
        )
        attendance.save()
        return attendance

# ========== Serializador para actualizar la Replay ==========


class UpdateAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['attendance']

    def update(self, instance, validated_data):
        attendance = super().update(instance, validated_data)
        return attendance

# ========== Serializador para eliminar la Replay ==========
class DeleteAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()

