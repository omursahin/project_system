from django.db import models


class GroupProject(models.Model):
    STATUS_CHOICES = (
        ('A', 'Approved'),
        ('P', 'Pending'),
        ('D', 'Draft'),
        ('R', 'Rejected'),
    )

    group = models.ForeignKey(
        'group.Group',
        on_delete=models.CASCADE, related_name='group')
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.BooleanField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'group_project'
        verbose_name = 'GroupProject'
        verbose_name_plural = 'GroupProjects'

    def __str__(self):
        return self.title
