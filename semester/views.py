from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from project_system.permissions import ReadOnly
from semester.models import Semester
from semester.serializers import SemesterSerializer


# Create your views here.
class SemesterList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
