# Generated by Django 4.2.16 on 2024-10-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unidentified_bodies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unidentifiedbody",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]