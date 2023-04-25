from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from report.models import Report
from report.serializers import ReportGetSerializer, ReportPostSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class ReportList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Report.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReportGetSerializer
        return ReportPostSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Report.objects.all()
    serializer_class = ReportGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReportGetSerializer
        return ReportPostSerializer
