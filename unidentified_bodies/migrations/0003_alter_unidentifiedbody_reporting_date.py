# Generated by Django 4.2.16 on 2024-10-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unidentified_bodies", "0002_alter_unidentifiedbody_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unidentifiedbody",
            name="reporting_date",
            field=models.DateField(),
        ),
    ]
