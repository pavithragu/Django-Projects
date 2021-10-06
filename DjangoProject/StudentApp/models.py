from django.db import models


# Create your models here.
class Students(models.Model):
    student_roll_number = models.IntegerField()
    student_name = models.CharField(max_length=25)
    student_class = models.IntegerField()
    student_address = models.CharField(max_length=50)
