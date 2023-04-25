from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from report.models import Report
from report.serializers import ReportSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class ReportList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer