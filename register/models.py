from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)


class Subject(models.Model):
    professor = models.ForeignKey(Professor)
    name = models.CharField(max_length=200)


class Student(models.Model):
    professor = models.ForeignKey(Professor)
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    school_grade = models.CharField(max_length=200)