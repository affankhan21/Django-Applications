from django.db import models

class Student(models.Model):
    sname=models.CharField(max_length=20)
    age=models.IntegerField()
    percentage=models.FloatField(default=60)

    class Meta:
        db_table="Student"
    def __str__(self):
        data=self.sname+","+str(self.age)+","+str(self.percentage)
        return data    
