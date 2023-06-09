# Generated by Django 4.1.7 on 2023-04-19 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "0003_alter_course_code_alter_course_description"),
        ("semester", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SemesterCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("max_group_size", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="semester.semester",
                    ),
                ),
            ],
            options={
                "verbose_name": "SemesterCourse",
                "verbose_name_plural": "SemesterCourses",
                "db_table": "semester_course",
                "unique_together": {("semester", "course")},
            },
        ),
    ]
