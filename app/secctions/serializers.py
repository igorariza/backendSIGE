from .models import (Secction,
                     Resource,
                     HyperLynks,
                     ResponseSecction,
                     Comment
                     )
# libreria serializers
from rest_framework import serializers
from users.serializers import StudentResponseSerializer

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

#======================Serializadores para la respuesta ================================================


class ResponseSecctionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResponseSecction
        fields = '__all__'
      


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

# ========== Serializador para eliminar la ResponseSecction ==========


class DeleteResponseSecctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseSecction
        fields = "__all__"

    def perform_destroy(self, instance):
        instance.delete()
        
#======================Serializadores para el comentario de la respuesta ================================================

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
        
        


# ========== Serializador para un SecctionSerializer =================================================================
class SecctionSerializer(serializers.ModelSerializer):

    resources = ResourceSerializer(many=True, read_only=True)
    lynks = HyperLynksSerializer(many=True, read_only=True)
    responses = ResponseSecctionbyAcademicchargeSerializer(many=True, read_only=True)

    class Meta:
        model = Secction
        fields = ['codeSecction',
                  'nameSecction',
                  'descriptionSecction',
                  'uploadOnSecction',
                  'workspaceSecction',
                  'resources',
                  'lynks',
                  'responses']
        
class SecctionStudentSerializer(serializers.ModelSerializer):
    
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
              
    

    class Meta:
        model = Secction
        fields = ['codeSecction',
                  'nameSecction',
                  'descriptionSecction',
                  'uploadOnSecction',
                  'workspaceSecction',
                  'resources',
                  'lynks',
                  'response']

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
