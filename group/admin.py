# Register your models here.
from django.contrib import admin

from group.models import Group


class GroupAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
            obj.max_size = obj.semester_course.max_group_size
        return super().save_model(request, obj, form, change)


admin.site.register(Group, GroupAdmin)
