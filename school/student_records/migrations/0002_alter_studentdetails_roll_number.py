# Generated by Django 3.2.6 on 2021-08-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='roll_number',
            field=models.IntegerField(max_length=6),
        ),
    ]