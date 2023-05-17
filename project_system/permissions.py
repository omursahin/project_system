from rest_framework.permissions import BasePermission, SAFE_METHODS

from group.models import Group


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsGroupOwner(BasePermission):
    def has_permission(self, request, view):
        group_id = request.data.get('group')
        if not group_id:
            return False
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return False
        return group.owner == request.user


class IsStudentOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        group_id = request.data.get('group')
        if not group_id:
            return False
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return False
        return group.owner == request.user
