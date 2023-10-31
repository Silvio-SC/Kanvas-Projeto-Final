from rest_framework import serializers
from .models import Course
from students_courses.serializers import StudentCourseSerializer
from contents.serializers import ContentSerializer


class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(
        many=True, allow_empty=True, required=False
        )
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
            'students_courses',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'instructor': {'required': False}
        }

        def update(self, instance, validated_data: dict):
            for key, value in validated_data.items():
                if key == "instructor" or 'contents' or 'id' or 'students':
                    pass
                else:
                    setattr(instance, key, value)

            instance.save()

            return instance


class AllCoursesSerializer(serializers.ModelSerializer):

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
            'students_courses',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'contents': {'read_only': True},
            'students_courses': {'read_only': True},
            'instructor': {'required': False}
        }


class StudentCourseReturnAllSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    students_courses = StudentCourseSerializer(many=True, allow_empty=True)
