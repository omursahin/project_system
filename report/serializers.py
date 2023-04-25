from rest_framework import serializers

from report.models import Report
from semester_course.serializers import SemesterCourseGetSerializer


class ReportGetSerializer(serializers.ModelSerializer):
    semester_course = SemesterCourseGetSerializer()

    class Meta:
        model = Report
        fields = '__all__'


class ReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
