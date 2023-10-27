from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.CourseView.as_view()),
    path('courses/<str:course_id>/', views.CourseDatailView.as_view()),
    # path('courses/<course_id:int>/students/')
]
