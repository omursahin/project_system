from rest_framework import serializers

from semester_course.models import SemesterCourse


class SemesterCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterCourse
        fields = '__all__'
