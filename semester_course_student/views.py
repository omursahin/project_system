from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from semester_course_student.models import SemesterCourseStudent
from semester_course_student.serializers \
    import SemesterCourseStudentGetSerializer, SemesterCourseStudentPostSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class SemesterCourseStudentList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = SemesterCourseStudent.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SemesterCourseStudentGetSerializer
        return SemesterCourseStudentPostSerializer


class SemesterCourseStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SemesterCourseStudent.objects.all()
    serializer_class = SemesterCourseStudentGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SemesterCourseStudentGetSerializer
        return SemesterCourseStudentPostSerializer
