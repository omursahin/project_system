from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from group_project.models import GroupProject
from group_project.serializers import GroupProjectSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class GroupProjectList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = GroupProject.objects.all()
    serializer_class = GroupProjectSerializer

    def perform_create(self, serializer):
        serializer.save(group=self.request.user.group)


class GroupProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = GroupProject.objects.all()
    serializer_class = GroupProjectSerializer

    def perform_update(self, serializer):
        serializer.save(group=self.request.user.group)
