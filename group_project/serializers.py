from rest_framework import serializers
from group_project.models import GroupProject


class GroupProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProject
        fields = '__all__'
