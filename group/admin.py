import uuid
from django.contrib import admin
from group.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'semester_course', 'title', 'description',
                    'max_size', 'status', 'invitation_code')
    list_filter = ('semester_course', 'status')
    search_fields = ('title', 'description', 'semester_course',)
    readonly_fields = ('invitation_code', 'max_size')

    fieldsets = (
        ('Group', {
            'fields': ('semester_course', 'title', 'description', 'max_size',
                       'status', 'invitation_code')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
            obj.max_size = obj.semester_course.max_group_size
            obj.invitation_code = str(uuid.uuid4())[:6].upper()
        return super().save_model(request, obj, form, change)


admin.site.register(Group, GroupAdmin)
