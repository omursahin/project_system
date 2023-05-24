from django.db import models


# Create your models here.
class GroupMember(models.Model):
    member = models.ForeignKey('account.MyUser', on_delete=models.CASCADE,
                               null=False, blank=False)
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE,
                              null=False, blank=False)
    is_accepted = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)

    class Meta:
        db_table = 'group_member'
        verbose_name = 'GroupMember'
        verbose_name_plural = 'GroupMembers'
        unique_together = ('member', 'group')

    def __str__(self):
        return "%s - %s" % (self.group.title,
                            self.member.identication_number)
