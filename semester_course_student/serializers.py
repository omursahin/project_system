from rest_framework import serializers

from project_system.urls import UserSerializer
from semester_course.serializers import SemesterCourseGetSerializer
from semester_course_student.models import SemesterCourseStudent


class SemesterCourseStudentGetSerializer(serializers.ModelSerializer):
    semester_course = SemesterCourseGetSerializer()
    student = UserSerializer()

    class Meta:
        model = SemesterCourseStudent
        fields = '__all__'


class SemesterCourseStudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterCourseStudent
        fields = '__all__'
