from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=20)
    age=models.IntegerField(default=20)
    percentage=models.FloatField(default=60)
    location=models.CharField(max_length=20)
    class Meta:
      db_table="Student"


