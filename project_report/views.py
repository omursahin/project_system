from rest_framework import generics
from rest_framework.permissions \
    import IsAuthenticated, IsAdminUser

from project_report.models import ProjectReport
from project_report.serializers \
    import ProjectReportGetSerializer, \
    ProjectReportPostSerializer
from project_system.permissions import ReadOnly


class ProjectReportList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | ReadOnly | IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return ProjectReport.objects.all()
        return ProjectReport.objects.filter(student=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectReportGetSerializer
        return ProjectReportPostSerializer


class ProjectReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly | IsAdminUser]
    serializer_class = ProjectReportGetSerializer

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return ProjectReport.objects.all()
        return ProjectReport.objects.filter(student=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectReportGetSerializer
        return ProjectReportPostSerializer
