from django.db import models


class Employee(models.Model):
    e_no = models.IntegerField()
    e_name = models.CharField(max_length=255)
    e_salary = models.FloatField()
    e_address = models.CharField(max_length=255)
