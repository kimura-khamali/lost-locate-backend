# Generated by Django 4.2 on 2024-09-14 07:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mortuary_staff", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UnidentifiedBody",
            fields=[
                ("id", models.SmallIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
                (
                    "skin_color",
                    models.CharField(
                        choices=[
                            ("light_skinned", "Light Skinned"),
                            ("dark_skinned", "Dark Skinned"),
                        ],
                        default="dark_skinned",
                        max_length=50,
                    ),
                ),
                ("weight", models.FloatField()),
                ("height", models.FloatField()),
                ("body_marks", models.TextField()),
                ("reporting_date", models.DateTimeField()),
                ("clothes_worn", models.TextField()),
                ("hair_color", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mortuary_staff.mortuarystaff",
                    ),
                ),
            ],
        ),
    ]
