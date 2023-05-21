from django.db import models

# Create your models here.

class ProjectReport(models.Model):
    project = models.ForeignKey('group_project.GroupProject',
                                        on_delete=models.CASCADE,
                                        null=False, blank=False)
    report = models.ForeignKey('report.Report', on_delete=models.CASCADE,
                                null=False, blank=False)

    description = models.CharField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    is_submitted = models.BooleanField
    version = models.IntegerField
    plagiarism_file = models.FileField(null=True, blank=True)
    plagiarism_rate = models.IntegerField(null=True, blank=True)
