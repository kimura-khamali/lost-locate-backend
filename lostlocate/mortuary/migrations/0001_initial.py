# Generated by Django 5.1 on 2024-09-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mortuary',
            fields=[
                ('mortuary_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('mortuary_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]