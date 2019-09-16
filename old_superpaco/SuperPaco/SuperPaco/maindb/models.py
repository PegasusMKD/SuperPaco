from django.db import models
from django.contrib.postgres.fields import ArrayField
        
# Create your models here.

class ID(models.Model):
    id_m = models.CharField(max_length=200)
    good_choices = models.PositiveIntegerField(default = 0)
    choices = models.TextField(default='')
#    choices = ArrayField(
#        ArrayField(
#            models.PositiveIntegerField(blank = True),
#            null = True,
#            default=list,
#            blank=True
#            ),
#    null = True,
#    blank=True,
#    default=list
#    )
    bad_choices = models.PositiveIntegerField(default = 0)
    activity = models.BooleanField(default=True)
    age = models.PositiveIntegerField(default = 0)
    gender = models.CharField(max_length=7)
    q1 = models.CharField(max_length=3)
    q2 = models.CharField(max_length=3)


    def __str__(self):
        return(self.id_m)

class Leftovers(models.Model):
    name = models.CharField(max_length=10,default="Leftovers")
    good_choices = models.PositiveIntegerField(default = 0)
    neutral_choices = models.PositiveIntegerField(default = 0)
    bad_choices = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return("Leftovers:" + self.name )
