from rest_framework import serializers

from report.serializers import ReportGetSerializer
from project_report.models import ProjectReport
from group_project.serializers import GroupProjectSerializer


class ProjectReportGetSerializer(serializers.ModelSerializer):
    report = ReportGetSerializer()
    project = GroupProjectSerializer()

    class Meta:
        model = ProjectReport
        fields = '__all__'


class ProjectReportPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectReport
        fields = '__all__'
