from django.urls import path
from semester_course_student.views \
    import SemesterCourseStudentList, \
    SemesterCourseStudentDetail

urlpatterns = [
    path('', SemesterCourseStudentList.as_view()),
    path('<int:pk>/', SemesterCourseStudentDetail.as_view()),
]
