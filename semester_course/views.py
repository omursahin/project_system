from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from semester_course.models import SemesterCourse
from semester_course.serializers import SemesterCourseGetSerializer, \
    SemesterCoursePostSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class SemesterCourseList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = SemesterCourse.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SemesterCourseGetSerializer
        return SemesterCoursePostSerializer


class SemesterCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = SemesterCourse.objects.all()
    serializer_class = SemesterCourseGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SemesterCourseGetSerializer
        return SemesterCoursePostSerializer
