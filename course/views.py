from rest_framework import generics
from rest_framework.permissions import BasePermission, \
    SAFE_METHODS, IsAuthenticated, IsAdminUser

from course.models import Course
from course.serializers import CourseSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# Create your views here.
class CourseList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
