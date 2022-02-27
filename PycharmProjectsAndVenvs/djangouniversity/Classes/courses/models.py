from django.db import models

# Create your models here.
#Here is a class for different school courses
class Course(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course = models.IntegerField(default="", blank=True, null=False)
    instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    description = models.TextField(max_length=400, default="", blank=True, null=False)

