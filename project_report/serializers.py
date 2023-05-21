from rest_framework import serializers

from report.serializers import ReportGetSerializer
from project_report.models import ProjectReport


class ProjectReportGetSerializer(serializers.ModelSerializer):
    report = ReportGetSerializer()

    class Meta:
        model = ProjectReport
        fields = '__all__'


class ProjectReportPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectReport
        fields = '__all__'




