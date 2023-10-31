from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response, status
from .models import Content
from courses.models import Course
from .serializers import ContentSerializer
from django.shortcuts import get_object_or_404

from drf_spectacular.utils import extend_schema

from courses.permissions import IsAdminOrOwner, IsAdminOrGet
from rest_framework_simplejwt.authentication import JWTAuthentication


@extend_schema(tags=['Contents'])
class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrGet]

    lookup_url_kwarg = "course_id"

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        if self.kwargs.get("course_id"):
            course = get_object_or_404(Course, pk=self.kwargs.get("course_id"))
            serializer.save(course=course)
        else:
            serializer.save()


@extend_schema(tags=['Contents'])
class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOwner]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    multiple_lookup_fields = ["course_id", "content_id"]

    def get_response(self, data, status_code):
        return Response(data, status=status_code)

    def get_object(self):
        queryset = self.get_queryset()

        filter = {
            'course_id': self.kwargs["course_id"],
            'id': self.kwargs["content_id"]
        }
        try:
            Course.objects.get(pk=self.kwargs["course_id"])
            Content.objects.get(pk=self.kwargs["content_id"])
            obj = get_object_or_404(queryset, **filter)
        except Course.DoesNotExist:
            return None
        except Content.DoesNotExist:
            return None

        self.check_object_permissions(self.request, obj)
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        course = Course.objects.filter(pk=self.kwargs["course_id"])
        content = Content.objects.filter(pk=self.kwargs["content_id"])

        if instance is None:
            if len(content) == 0:
                return Response({'detail': 'content not found.'}, status=status.HTTP_404_NOT_FOUND)
            elif len(course) == 0:
                return Response({'detail': 'course not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
