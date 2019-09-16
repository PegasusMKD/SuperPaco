from django.db import models
from django.contrib.postgres.fields import ArrayField,DateTimeRangeField
from postgres_copy import CopyManager


class User(models.Model):
    objects = CopyManager()
    user_hash = models.CharField(max_length=200)

    age = models.PositiveIntegerField(default = 0)
    gender = models.CharField(max_length=7)
    q1 = models.CharField(max_length=3)
    q2 = models.CharField(max_length=3)

    activity = models.BooleanField(default=True)
    time_stamps = ArrayField(
        models.CharField(max_length=45),
        blank=True,
        null=True,
        default=list
    )

    good_choices = models.PositiveIntegerField(default = 0)
    bad_choices = models.PositiveIntegerField(default = 0)

    choices = ArrayField(
        models.CharField(max_length=40),
        blank=True,
        null=True,
        default=list
        )



    def __str__(self):
        return(self.id_m)

class Leftovers(models.Model):
    name = models.CharField(max_length=10,default="Leftovers")
    good_choices = models.PositiveIntegerField(default = 0)
    neutral_choices = models.PositiveIntegerField(default = 0)
    bad_choices = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return("Leftovers:" + self.name )
