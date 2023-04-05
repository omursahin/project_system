from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated, IsAdminUser

from semester.models import Semester
from semester.serializers import SemesterSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# Create your views here.
class SemesterList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
