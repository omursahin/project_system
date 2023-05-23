from rest_framework import generics
from rest_framework.permissions \
    import IsAuthenticated

from project_report.models import ProjectReport
from project_report.serializers \
    import ProjectReportGetSerializer, \
    ProjectReportPostSerializer
from project_system.permissions \
    import IsProjectGroupOwner


class ProjectReportList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated | IsProjectGroupOwner]
    queryset = ProjectReport.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectReportGetSerializer
        return ProjectReportPostSerializer


class ProjectReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsProjectGroupOwner]
    queryset = ProjectReport.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectReportGetSerializer
        return ProjectReportPostSerializer
