from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.models import Course
from accounts.models import Account
from students_courses.models import StudentCourse

from courses.serializers import CourseSerializer, AllCoursesSerializer
from django.shortcuts import get_object_or_404

from .permissions import IsAdminOrOwner, IsAdminOrGet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrGet]

    serializer_class = AllCoursesSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Course.objects.all()
        else:
            studentCourse = StudentCourse.objects.filter(student=user.id)
            course_ids = studentCourse.values_list('course', flat=True)
            queryset = Course.objects.filter(id__in=course_ids)

        return queryset

    def perform_create(self, serializer):
        if self.kwargs.get("instructor"):
            instructor = get_object_or_404(Account, pk=self.kwargs.get("pk"))
            serializer.save(instructor_id=instructor)
        else:
            serializer.save()


class CourseDatailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    lookup_url_kwarg = "course_id"
