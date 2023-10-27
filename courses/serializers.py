from rest_framework import serializers
from .models import Course
from accounts.serializers import AccountSerializer
from contents.serializers import ContentSerializer


class CourseSerializer(serializers.ModelSerializer):
    students = AccountSerializer(many=True, allow_empty=True, required=False)
    contents = ContentSerializer(many=True, allow_empty=True, required=False)

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'status',
            'start_date',
            'end_date',
            'instructor',
            'contents',
            'students',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'contents': {'read_only': True},
            'instructor': {'required': False, 'source': 'instructor_id'}
        }

        def update(self, instance, validated_data: dict):
            for key, value in validated_data.items():
                if key == "instructor" or 'contents' or 'id' or 'students':
                    pass
                else:
                    setattr(instance, key, value)

            instance.save()

            return instance
