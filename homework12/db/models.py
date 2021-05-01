from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class HomeWork(models.Model):
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField()


class HomeworkResult(models.Model):
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    solution = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField()
