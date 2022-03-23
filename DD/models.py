from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.TextField()
    description = models.TextField()
    url = models.URLField()
    due_data = models.DateTimeField()
    grade = models.TextField()


class Groups(models.Model):
    title = models.TextField()
    users = models.TextField()
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)


class Theory(models.Model):
    title = models.TextField()
    doc = models.FileField(upload_to='theory/')
    upload_date = models.DateTimeField()
    subject = models.TextField()
    assigned_groups = models.ForeignKey(Groups, on_delete=models.CASCADE)
    summary = models.TextField(default='Short summary of the lecture')


class Subjects(models.Model):
    title = models.TextField()
    description = models.TextField()
    theories = models.ForeignKey(Theory, on_delete=models.CASCADE)


class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    photo = models.ImageField(upload_to='images/')
    subjects = models.ForeignKey(Subjects, related_name="subjects", on_delete=models.CASCADE)
    groups = models.ForeignKey(Groups, related_name="groups", on_delete=models.CASCADE)
    role = models.TextField()


class Practice(models.Model):
    title = models.TextField()
    description = models.TextField(default='Short summary')
    file = models.FileField(upload_to='practice/')
    subjects = models.ForeignKey(Subjects, related_name="subjects_practice", on_delete=models.CASCADE)
