from django.db import models
from course.models import Course
from semester.models import Semester


class SemesterCourse(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,
                                 null=False, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               null=False, blank=True)
    max_group_size = models.IntegerField(null=False, blank=True)

    class Meta:
        db_table = 'semester_course'
        verbose_name = 'SemesterCourse'
        verbose_name_plural = 'SemesterCourses'
        unique_together = ('semester', 'course',)

    def _str_(self):
        return self.semester.term + " " + self.course.title
