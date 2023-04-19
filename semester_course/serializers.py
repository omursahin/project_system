from rest_framework import serializers

from course.serializers import CourseSerializer
from semester.serializers import SemesterSerializer
from semester_course.models import SemesterCourse


class SemesterCourseGetSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer()
    course = CourseSerializer()

    class Meta:
        model = SemesterCourse
        fields = '__all__'


class SemesterCoursePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SemesterCourse
        fields = '__all__'
