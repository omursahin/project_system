from django.db import models
# Create your models here.


class Semester(models.Model):

    TERM_CHOICES = (
        (0, "Fall"),
        (1, "Spring"),
        (2, "Summer")
    )

    term = models.IntegerField(choices=TERM_CHOICES, default=1)
    year = models.IntegerField()

    class Meta:
        unique_together = ('term', 'year')
        db_table = 'semester'
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    def __str__(self):
        return str(self.year) + "-" + str(self.year + 1) + " " + \
               self.TERM_CHOICES.__getitem__(self.term).__getitem__(1) + \
               " Semester"
