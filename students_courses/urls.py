from django.urls import path
from .views import StudentsView


urlpatterns = [
    path('courses/<str:course_id>/students/', StudentsView.as_view())
]
