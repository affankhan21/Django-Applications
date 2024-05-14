from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=20)
    age = models.IntegerField()
    percentage = models.FloatField(default=60)
    location = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "Student"
