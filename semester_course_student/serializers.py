from rest_framework import serializers

from semester_course_student.models import SemesterCourseStudent


class SemesterCourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterCourseStudent
        fields = '__all__'
