from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("group", "0002_alter_group_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupProject",
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
                ("title", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_approved", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Approved"),
                            ("P", "Pending"),
                            ("D", "Draft"),
                            ("R", "Rejected"),
                        ],
                        default="D",
                        max_length=1,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="group",
                        to="group.group",
                    ),
                ),
            ],
            options={
                "verbose_name": "GroupProject",
                "verbose_name_plural": "GroupProjects",
                "db_table": "group_project",
            },
        ),
    ]
