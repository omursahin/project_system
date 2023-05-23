from rest_framework.permissions import BasePermission, SAFE_METHODS

from group.models import Group
from project_report.models import ProjectReport


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


class IsProjectGroupOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        project_id = request.data.get('project')
        if not project_id:
            return False

        try:
            project = ProjectReport.objects.get(id=project_id)
        except ProjectReport.DoesNotExist:
            return False

        group = project.group
        if not group:
            return False

        if group.owner == request.user:
            return True

        return False
