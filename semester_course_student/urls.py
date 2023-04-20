from django.urls import path
from semester_course_student.views import SemesterCourseStudentList, SemesterCourseStudentDetail

urlpatterns = [
    path('semester_course_students/', SemesterCourseStudentList.as_view()),
    path('semester_course_students/<int:pk>/', SemesterCourseStudentDetail.as_view()),
]
