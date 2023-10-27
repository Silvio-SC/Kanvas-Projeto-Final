from rest_framework import serializers
from .models import Course
from accounts.serializers import AccountSerializer
from courses.serializers import CourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    student = AccountSerializer()

    class Meta:
        model = Course
        fields = [
            'id',
            'status',
            'course',
            'student',
        ]
        extra_kwargs = {
            'status': {'max_length': 20},
            'id': {'read_only': True},
        }
