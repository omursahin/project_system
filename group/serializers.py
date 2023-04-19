from rest_framework import serializers
from group.models import Group
from project_system.urls import UserSerializer
from semester_course.serializers import SemesterCourseGetSerializer
import uuid


class GroupGetSerializer(serializers.ModelSerializer):
    semester_course = SemesterCourseGetSerializer()
    owner = UserSerializer()

    class Meta:
        model = Group
        fields = '__all__'


class GroupPostSerializer(serializers.ModelSerializer):
    invitation_code = serializers.ReadOnlyField()

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('id', 'owner', 'max_size', 'invitation_code')

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['owner'] = request.user
        validated_data['max_size'] = \
            validated_data['semester_course'].max_group_size
        validated_data['invitation_code'] = str(uuid.uuid4())[:6].upper()
        return super().create(validated_data)
