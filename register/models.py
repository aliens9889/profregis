from django.db import models


class Professor(models.Model):
    professor_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)

    def __str__(self):
        return self.professor_name


class Course(models.Model):
    professor = models.ForeignKey(Professor)
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    professor = models.ForeignKey(Professor)
    subject = models.ForeignKey(Subject)
    student_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    school_grade = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name
