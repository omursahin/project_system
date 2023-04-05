from django.db import models
# Create your models here.


class Semester(models.Model):

    TERM_CHOICES = (
        (0, "Fall"),
        (1, "Spring"),
        (2, "Summer")
    )

    term = models.CharField(max_length=9,
                            choices=TERM_CHOICES,
                            default=1)
    year = models.IntegerField()

    class Meta:
        unique_together = ('term', 'year')
        db_table = 'semester'
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    def __str__(self):
        return str(self.year) + "-" + str(self.year + 1) + \
               " " + self.term + " Semester"
