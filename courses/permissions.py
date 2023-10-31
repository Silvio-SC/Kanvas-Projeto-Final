from rest_framework import permissions
from rest_framework.views import Request, View
from students_courses.models import StudentCourse


class IsAdminOrGet(permissions.BasePermission):
    def has_permission(self, request, view):

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):

        return request.user.is_superuser


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        user_id = request.user.id
        if request.method in permissions.SAFE_METHODS:
            students_list = StudentCourse.objects.filter(
                course_id=view.kwargs['course_id']
                )
            for student in students_list:
                if student.student_id == user_id:
                    return True

        return request.user.is_superuser
