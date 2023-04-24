from django.db import models


class Group(models.Model):
    STATUS_CHOICES = (("A", "Approved"),
                      ("P", "Pending"),
                      ("D", "Draft"),
                      ("R", "Rejected"))

    owner = models.ForeignKey('account.MyUser', on_delete=models.CASCADE,
                              editable=False, related_name='owner_groups')
    semester_course = models.ForeignKey(
        'semester_course.SemesterCourse',
        on_delete=models.CASCADE, related_name='semester_course')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    max_size = models.IntegerField(editable=False)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='active')
    invitation_code = models.CharField(
        max_length=6, editable=False, unique=True)

    class Meta:
        db_table = 'group'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.title
