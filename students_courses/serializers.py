from rest_framework import serializers
from .models import StudentCourse
from courses.models import Course


class StudentCourseSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    student_id = serializers.UUIDField(source='student.id', read_only=True)
    student_username = serializers.CharField(read_only=True, source='student.username')
    student_email = serializers.EmailField(read_only=True, source='student.email')
    status = serializers.CharField(read_only=True)

    class Meta:
        model = StudentCourse
        fields = [
            'id',
            'student_id',
            'student_username',
            'student_email',
            'status'
        ]


class StudentCourseWithoutReadOnlySerializer(StudentCourseSerializer):
    id = serializers.UUIDField()
    student_id = serializers.UUIDField(source='id')
    student_username = serializers.CharField(source='username')
    student_email = serializers.EmailField(source='email')
    status = serializers.CharField()


class StudentCourseReturnSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    students_courses = StudentCourseWithoutReadOnlySerializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'students_courses'
        ]
