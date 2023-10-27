from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    course = serializers.CharField()

    class Meta:
        model = Content
        fields = [
            'id',
            'name',
            'content',
            'video_url',
        ]
        extra_kwargs = {
            'video_url': {'allow_null': True},
            'content': {'allow_blank': True, 'default': ''},
            'id': {'read_only': True},
        }
