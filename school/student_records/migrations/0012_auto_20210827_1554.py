# Generated by Django 3.2.6 on 2021-08-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0011_remove_onlinepayment_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinepayment',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='onlinepayment',
            name='username',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]