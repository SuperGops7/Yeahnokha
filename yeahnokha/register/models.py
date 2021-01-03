from django.db import models
import datetime

# Create your models here.

class Register(models.Model):
    part_name = models.CharField(max_length = 40)
    part_inst = models.CharField(max_length = 50)
    part_email = models.EmailField(max_length = 50)
    part_phone = models.CharField(max_length = 12) 
    part_DOB = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title