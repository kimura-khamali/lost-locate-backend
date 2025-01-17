# Generated by Django 4.2 on 2024-09-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MissingPerson",
            fields=[
                ("id", models.SmallIntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(default="Unknown", max_length=100)),
                ("age", models.SmallIntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=50,
                    ),
                ),
                ("contact", models.CharField(max_length=50)),
                ("image", models.CharField(max_length=50)),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
                ("hair_color", models.CharField(max_length=50)),
                (
                    "eye_color",
                    models.CharField(
                        choices=[("black", "Black"), ("brown", "Brown")],
                        default="black",
                        max_length=50,
                    ),
                ),
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
                ("missing_date", models.DateField()),
                ("location", models.CharField(max_length=50)),
                ("clothes_worn", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
