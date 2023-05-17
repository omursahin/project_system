from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from group_member.models import GroupMember
from group_member.serializer import GroupMemberGetSerializer,\
    GroupMemberPostSerializer


class GroupMemberList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GroupMember.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupMemberGetSerializer
        return GroupMemberPostSerializer


class GroupMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupMemberGetSerializer
        return GroupMemberPostSerializer
