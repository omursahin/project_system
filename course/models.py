from django.db import models


class Course(models.Model):
    code = models.CharField(unique=True, null=False,
                            blank=False, max_length=10)
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=1000)

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.code + " " + self.title
