from .models import (
    Course,
    Area,
    AcademicCharge,
    TimeTable
)
# libreria serializers
from rest_framework import serializers

# ========== Serializador para una Area =================================================================


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


# ========== Serializador para crear la Area ==========
class CreateAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ['codeArea', 'nameArea']

    def create(self, validated_data):
        area = Area.objects.create(
            nameArea    =validated_data['nameArea'],
        )
        area.save()
        return area

# ========== Serializador para actualizar la Area ==========


class UpdateAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = "__all__"

    def update(self, instance, validated_data):
        area = super().update(instance, validated_data)
        return area

# ========== Serializador para eliminar la Area ==========


class DeleteAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()

# ========== Serializador para un Curso =================================================================


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


# ========== Serializador para crear la Curso ==========
class CreateCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['nameCourse',
                  'areaCourse']

    def create(self, validated_data):
        course = Course.objects.create(
            nameCourse=validated_data['nameCourse'],
            areaCourse=validated_data['areaCourse']
        )
        course.save()
        return course

# ========== Serializador para actualizar la Curso ==========


class UpdateCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def update(self, instance, validated_data):
        course = super().update(instance, validated_data)
        return course

# ========== Serializador para eliminar la Curso ==========


class DeleteCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para un Horario =================================================================


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'


# ========== Serializador para crear la Horario ==========
class CreateTimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeTable
        fields = ['dayTimeTable', 'startHourTimeTable',
                  'endHourTimeTable', 'courseTimeTable']

    def create(self, validated_data):
        timetable = TimeTable.objects.create(
            dayTimeTable=validated_data['dayTimeTable'],
            startHourTimeTable=validated_data['startHourTimeTable'],
            endHourTimeTable=validated_data['endHourTimeTable'],
            courseTimeTable=validated_data['courseTimeTable']
        )
        timetable.save()
        return timetable

# ========== Serializador para actualizar la Horario ==========


class UpdateTimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeTable
        fields = "__all__"

    def update(self, instance, validated_data):
        timetable = super().update(instance, validated_data)
        return timetable

# ========== Serializador para eliminar la Horario ==========


class DeleteTimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeTable
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para la Carga Academica =================================================================


class AcademicChargeSerializer(serializers.ModelSerializer):

    schedule = TimeTableSerializer(many=True, read_only=True)

    class Meta:
        model = AcademicCharge
        fields = ['codeAcademicCharge',
                  'teacherDictate',
                  'courseDictate',
                  'groupDictate',
                  'hourlyintensity', 'schedule']


# ========== Serializador para crear la Carga Academica ==========
class CreateAcademicChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicCharge
        fields = ['teacherDictate',
                  'courseDictate',
                  'groupDictate',
                  'hourlyintensity']

    def create(self, validated_data):
        academiccharge = AcademicCharge.objects.create(
            teacherDictate=validated_data['teacherDictate'],
            courseDictate=validated_data['courseDictate'],
            groupDictate=validated_data['groupDictate'],
            hourlyintensity=validated_data['hourlyintensity']
        )
        academiccharge.save()
        return academiccharge

# ========== Serializador para actualizar la Carga Academica ==========


class UpdateAcademicChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicCharge
        fields = "__all__"

    def update(self, instance, validated_data):
        academiccharge = super().update(instance, validated_data)
        return academiccharge

# ========== Serializador para eliminar la Carga Academica ==========


class DeleteAcademicChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcademicCharge
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


