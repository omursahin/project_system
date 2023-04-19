import uuid

from rest_framework import serializers

from group.models import Group



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'owner', 'semester_course', 'title', 'description', 'max_size', 'status', 'invitation_code')
        read_only_fields = ('id', 'owner', 'max_size', 'invitation_code')

    def validate_semester_course(self, value):
        if not value:
            raise serializers.ValidationError("Please enter a valid semester course")
        return value

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        validated_data['max_size'] = validated_data['semester_course'].max_group_size
        validated_data['invitation_code'] = str(uuid.uuid4())[:6].upper()
        return super().create(validated_data)
