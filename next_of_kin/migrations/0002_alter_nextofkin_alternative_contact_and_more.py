# Generated by Django 4.2.16 on 2024-10-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("next_of_kin", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nextofkin",
            name="alternative_contact",
            field=models.CharField(default="Unknown", max_length=30),
        ),
        migrations.AlterField(
            model_name="nextofkin",
            name="contact",
            field=models.CharField(max_length=30),
        ),
    ]
