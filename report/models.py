from django.db import models


class Report(models.Model):
    semester_course = models.ForeignKey('semester_course.SemesterCourse',
                                        on_delete=models.CASCADE,
                                        null=False, blank=False)
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    is_public = models.BooleanField(default=False)
    is_final = models.BooleanField(default=False)

    class Meta:
        db_table = 'report'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return str(self.semester_course) + " - " + self.title
