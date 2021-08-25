from django.db import models


class StudentDetails(models.Model):
    student_name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    DOB = models.DateField()


def __srt__(self):
    return self.student_name


class StudentMarkDetails(models.Model):
    stud_name = models.CharField(max_length=30)
    stud_roll_no = models.CharField(max_length=15, unique=True)
    Tamil = models.CharField(max_length=3)
    English = models.CharField(max_length=3)
    Mathematical = models.CharField(max_length=3)
    Science = models.CharField(max_length=3)
    Social_science = models.CharField(max_length=3)
    Total = models.IntegerField()


def __str__(self):
    return self.stud_name
