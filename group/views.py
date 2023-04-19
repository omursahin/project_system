from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from group.models import Group
from group.serializers import GroupGetSerializer, GroupPostSerializer


class GroupList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupGetSerializer
        return GroupPostSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupGetSerializer
        return GroupPostSerializer
