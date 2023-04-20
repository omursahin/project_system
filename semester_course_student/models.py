from django.db import models


# Create your models here.
class SemesterCourseStudent(models.Model):
    semester_course = models.ForeignKey('semester_course.SemesterCourse', on_delete=models.CASCADE,
                                        null=False, blank=False)
    student = models.ForeignKey('account.MyUser', on_delete=models.CASCADE,
                                null=False, blank=False)
    mid_term = models.IntegerField(null=False, blank=False)
    final = models.IntegerField(null=False, blank=False)
