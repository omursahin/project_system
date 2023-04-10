from django.urls import path

import course
from course.views import CourseList, CourseDetail

urlpatterns = [
    path('', CourseList.as_view()),
    path('<int:pk>/', CourseDetail.as_view()),
]
