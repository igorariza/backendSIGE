from .models import ImageResponse
# libreria serializers
from rest_framework import serializers


class ImageResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageResponse
        fields = '__all__'


class CreateImageResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageResponse
        fields = '__all__'

    def create(self, validated_data):
        image = ImageResponse.objects.create(
            name=validated_data['name'],
            response=validated_data['response'],
            url=validated_data['url']
        )
        image.save()
        return image


class DeleteImageResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageResponse
        fields = "__all__"
        
    def perform_destroy(self, instance):
        instance.delete()
