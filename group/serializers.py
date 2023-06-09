from rest_framework import serializers
from group.models import Group
from group_member.models import GroupMember
from group_project.models import GroupProject
from project_system.urls import UserSerializer
from semester_course.serializers import SemesterCourseGetSerializer
import uuid


class GroupMemberSerializer(serializers.ModelSerializer):
    member = UserSerializer()

    class Meta:
        model = GroupMember
        fields = '__all__'


class GroupProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProject
        fields = '__all__'


class GroupGetSerializer(serializers.ModelSerializer):
    semester_course = SemesterCourseGetSerializer()
    owner = UserSerializer()
    group_members = serializers.SerializerMethodField()
    group_projects = serializers.SerializerMethodField()

    def get_group_members(self, obj):
        group_members = GroupMember.objects.filter(group_id=obj.id).all()
        return GroupMemberSerializer(group_members, many=True,
                                     context=self.context).data

    def get_group_projects(self, obj):
        group_projects = GroupProject.objects.filter(group_id=obj.id).all()
        return GroupProjectSerializer(group_projects, many=True,
                                      context=self.context).data

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
