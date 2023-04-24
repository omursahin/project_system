from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsStaff

from semester_course_student.models import SemesterCourseStudent
from semester_course_student.serializers import SemesterCourseStudentSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class SemesterCourseStudentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | IsStaff | ReadOnly]
    queryset = SemesterCourseStudent.objects.all()
    serializer_class = SemesterCourseStudentSerializer


class SemesterCourseStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | IsStaff | ReadOnly]
    queryset = SemesterCourseStudent.objects.all()
    serializer_class = SemesterCourseStudentSerializer
