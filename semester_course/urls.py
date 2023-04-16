from django.urls import path

from semester_course.views import SemesterCourseList, SemesterCourseDetail

urlpatterns = [
    path('', SemesterCourseList.as_view()),
    path('<int:pk>/', SemesterCourseDetail.as_view()),
]