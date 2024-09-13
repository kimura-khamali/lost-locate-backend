# Generated by Django 4.2 on 2024-09-13 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('missing_persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(default='Unknown', max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('alternative_contact', models.CharField(default='Unknown', max_length=15)),
                ('missing_person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missing_persons.missingperson')),
            ],
        ),
    ]