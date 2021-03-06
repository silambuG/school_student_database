# Generated by Django 3.2.6 on 2021-08-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0003_alter_studentdetails_roll_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarkDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=30)),
                ('stud_roll_no', models.CharField(max_length=15)),
                ('Tamil', models.CharField(max_length=3)),
                ('English', models.CharField(max_length=3)),
                ('Mathematical', models.CharField(max_length=3)),
                ('Science', models.CharField(max_length=3)),
                ('Social_science', models.CharField(max_length=3)),
                ('Total', models.IntegerField()),
            ],
        ),
    ]
