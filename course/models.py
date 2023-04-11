from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    # course_credit = models.IntegerField()

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.code + " " + self.title
