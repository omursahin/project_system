# Generated by Django 4.1.7 on 2023-05-10 13:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("semester_course", "0001_initial"),
        ("semester_course_student", "0003_alter_semestercoursestudent_final_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="semestercoursestudent",
            unique_together={("semester_course", "student")},
        ),
    ]
