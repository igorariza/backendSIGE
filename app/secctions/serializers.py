# libreria serializers
from rest_framework import serializers
from users.serializers import StudentResponseSerializer
from images.serializers import ImageResponseSerializer
from .models import (
    Secction,
    Resource,
    HyperLynks,
    ResponseSecction,
    Comment,
    Responses,
    Homework
)

# ========== Serializador para una Resource =================================================================


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['codeResouce', 'resource', 'secctionResource']

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


# ======================Serializadores para el comentario de la respuesta ================================================

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# ========== Serializador para crear la Comment ==========
class CreateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment = Comment.objects.create(
            teacherComment=validated_data['teacherComment'],
            comment=validated_data['comment'],
            responseToComment=validated_data['responseToComment']
        )
        comment.save()
        return comment

# ========== Serializador para actualizar la Comment ==========


class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment']

    def update(self, instance, validated_data):
        comment = super().update(instance, validated_data)
        return comment

# ========== Serializador para eliminar la Comment ==========


class DeleteCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


# ======================Serializadores para la respuesta ================================================


class ResponseSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseSecction
        fields = ['codeResponse',
                  'secctionResponse',
                  'response',
                  'messageResponse',
                  'dateResponse',
                  'studentResponse',
                  ]


class ResponseSecctionbyAcademicchargeSerializer(serializers.ModelSerializer):

    studentResponse = StudentResponseSerializer()

    class Meta:
        model = ResponseSecction
        fields = ['codeResponse',
                  'secctionResponse',
                  'response',
                  'messageResponse',
                  'dateResponse',
                  'studentResponse'
                  ]


class DeleteResponseSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseSecction
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para actualizar la ResponseSecction ==========


class UpdateResponseSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseSecction
        fields = ['messageResponse']

    def update(self, instance, validated_data):
        responseSecction = super().update(instance, validated_data)
        return responseSecction


# ========== Serializador para una Resource =================================================================


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['code_homework', 'response_secction', 'response_file']

# ========== Serializador para eliminar la Resource ==========


class DeleteHomeworkSerializers(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()


# ======================Serializadores para la respuesta ================================================


class ResponsesSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(read_only=True)
    response = HomeworkSerializer(read_only=True)

    class Meta:
        model = Responses
        fields = ['code_response',
                  'secction_response',
                  'message_response',
                  'date_response',
                  'student_response',
                  'comment',
                  'response'
                  ]


class CreateResponsesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responses
        fields = '__all__'

    def create(self, validated_data):
        response = Responses.objects.create(
            secction_response=validated_data['secction_response'],
            message_response=validated_data['message_response'],
            student_response=validated_data['student_response']
        )
        response.save()
        return response


class ResponsesbyAcademicchargeSerializer(serializers.ModelSerializer):

    student_response = StudentResponseSerializer(read_only=True)
    comment = CommentSerializer(read_only=True)
    homework = HomeworkSerializer(many=True, read_only=True)
    images = ImageResponseSerializer(read_only=True, many=True)

    class Meta:
        model = Responses
        fields = ['code_response',
                  'secction_response',
                  'message_response',
                  'date_response',
                  'student_response',
                  'comment',
                  'homework',
                  'images'
                  ]


class DeleteResponsesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responses
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()


# ========== Serializador para actualizar la ResponseSecction ==========


class UpdateResponsesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responses
        fields = [
            'message_response'
        ]

    def update(self, instance, validated_data):
        response = super().update(instance, validated_data)
        return response

# ========== Serializador para un SecctionSerializer =================================================================


class SecctionSerializer(serializers.ModelSerializer):

    resources = ResourceSerializer(many=True, read_only=True)
    lynks = HyperLynksSerializer(many=True, read_only=True)
    response = ResponsesbyAcademicchargeSerializer(
        many=True, read_only=True)

    class Meta:
        model = Secction
        fields = ['codeSecction',
                  'nameSecction',
                  'descriptionSecction',
                  'uploadOnSecction',
                  'date_close',
                  'image_found',
                  'workspaceSecction',
                  'resources',
                  'lynks',
                  'response']


class SecctionStudentSerializer(serializers.ModelSerializer):

    resources = ResourceSerializer(many=True, read_only=True)
    lynks = HyperLynksSerializer(many=True, read_only=True)
    responses = ResponsesSerializer(read_only=True)

    class Meta:
        model = Secction
        fields = ['codeSecction',
                  'nameSecction',
                  'image_found',
                  'descriptionSecction',
                  'uploadOnSecction',
                  'date_close',
                  'workspaceSecction',
                  'resources',
                  'lynks',
                  'responses']

# ========== Serializador para crear el SecctionSerializer ==========


class CreateSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secction
        fields = '__all__'

    def create(self, validated_data):
        secction = Secction.objects.create(
            nameSecction=validated_data['nameSecction'],
            descriptionSecction=validated_data['descriptionSecction'],
            date_close=validated_data['date_close'],
            image_found=validated_data['image_found'],
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
                  'date_close',
                  'image_found',
                  'descriptionSecction']

    def update(self, instance, validated_data):
        secction = super().update(instance, validated_data)
        return secction

# ========== Serializador para eliminar la IE ==========


class DeleteSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secction
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()
