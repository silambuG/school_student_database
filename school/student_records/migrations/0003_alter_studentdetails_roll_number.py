# Generated by Django 3.2.6 on 2021-08-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0002_alter_studentdetails_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='roll_number',
            field=models.IntegerField(),
        ),
    ]