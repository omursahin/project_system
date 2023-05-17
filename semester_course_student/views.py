from rest_framework import generics

from rest_framework.permissions import IsAdminUser

from project_system.permissions import ReadOnly
from semester_course_student.models import SemesterCourseStudent
from semester_course_student.serializers \
    import SemesterCourseStudentGetSerializer, \
    SemesterCourseStudentPostSerializer


# Create your views here.
class SemesterCourseStudentList(generics.ListCreateAPIView):
    # TODO: student veya staff okuyabilir
    permission_classes = [ReadOnly | IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return SemesterCourseStudent.objects.all()
        return SemesterCourseStudent.objects.filter(student=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SemesterCourseStudentGetSerializer
        return SemesterCourseStudentPostSerializer


class SemesterCourseStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly | IsAdminUser]
    serializer_class = SemesterCourseStudentGetSerializer

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return SemesterCourseStudent.objects.all()
        return SemesterCourseStudent.objects.filter(student=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SemesterCourseStudentGetSerializer
        return SemesterCourseStudentPostSerializer
