from django.db import models


class Employee(models.Model):
    name = models.CharField()