from django.db import models
import datetime

# Create your models here.
class Event(models.Model):
    CATEGORIES = (
        ('UG' , 'UnderGraduates'),
        ('PG' , 'PostGraduates'),
        ('ST' , 'Staff'),
        ('SC' , 'School Students')
    )
    category = models.CharField(max_length = 2, choices = CATEGORIES)
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    date = models.DateField(default=datetime.date.today)
    fees = models.IntegerField(default = 100)

    def __str__(self):
        return self.title

