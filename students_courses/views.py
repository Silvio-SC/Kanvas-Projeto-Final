from django.forms import model_to_dict
from rest_framework.views import APIView, Response, Request, status
from courses.models import Course
from accounts.models import Account
from .models import StudentCourse
from courses.serializers import StudentCourseReturnAllSerializer
from .serializers import (
    StudentCourseSerializer,
    StudentCourseReturnSerializer
    )
from django.shortcuts import get_object_or_404
from courses.permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]

    def get(self, req: Request, course_id: str) -> Response:
        course = get_object_or_404(Course, id=course_id)
        serializer = StudentCourseReturnAllSerializer(instance=course)

        return Response(serializer.data, 200)

    def put(self, req: Request, course_id: str) -> Response:
        course = get_object_or_404(Course, id=course_id)
        serializer1 = StudentCourseReturnAllSerializer(instance=course)

        Not_found_students_list = []

        for student in req.data['students_courses']:
            try:
                find_student = Account.objects.get(email=student['student_email'])
            except Account.DoesNotExist:
                Not_found_students_list.append(student['student_email'])

        if len(Not_found_students_list) > 0:
            strg_list = ", ".join(Not_found_students_list)
            return Response({
	            "detail": "No active accounts was found: " + strg_list + "."
            }, status.HTTP_400_BAD_REQUEST)

        for student in req.data['students_courses']:
            find_student = Account.objects.get(email=student['student_email'])

            serializer = StudentCourseSerializer(
                many=True,
                data=req.data['students_courses']
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(course=course, student=find_student)

        return Response(serializer1.data, status=status.HTTP_200_OK)
