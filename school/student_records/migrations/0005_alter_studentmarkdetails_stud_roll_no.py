# Generated by Django 3.2.6 on 2021-08-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0004_studentmarkdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarkdetails',
            name='stud_roll_no',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]