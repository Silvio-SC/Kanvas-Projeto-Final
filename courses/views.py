from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.models import Course
from accounts.models import Account
from courses.serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrGet, IsAdminOrOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrGet]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

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
