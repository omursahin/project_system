from rest_framework import serializers

from group.serializers import GroupGetSerializer
from group_member.models import GroupMember
from project_system.urls import UserSerializer


class GroupMemberGetSerializer(serializers.ModelSerializer):
    group = GroupGetSerializer()
    member = UserSerializer()

    class Meta:
        model = GroupMember
        fields = '__all__'


class GroupMemberPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupMember
        fields = '__all__'
