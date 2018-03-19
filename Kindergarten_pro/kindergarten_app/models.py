from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carer(models.Model):
    CONNECTION = (
        (-1, "undefined"),
        (1, "mother"),
        (2, "father"),
        (3, "foster_parent")
    )
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=10)
    family_connection = models.IntegerField(choices=CONNECTION, default=-1)


class Child(models.Model):
    KINDERGARTEN_GROUPS = {
        (0, "Nieokreślona"),
        (1, "Grupa Zielona"),
        (2, "Grupa Niebieska"),
    }

    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    year_of_birth = models.IntegerField(null=True)
    group = models.IntegerField(choices=KINDERGARTEN_GROUPS, default=0)
    carers = models.ManyToManyField(Carer)

    @property
    def name(self):
        return "{} {} {}".format(self.first_name, self.second_name, self.last_name)

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=64)
    member = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True)


class Teacher(models.Model):
    TYPES = (
        (-1, "undefined"),
        (1, "pre-school educator"),
        (2, "pedagogue"),
        (3, "psychologist"),
        (4, "pre-school help"),
        (5, "pre-school teacher"),
    )

    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=10)
    type_of_teacher = models.IntegerField(choices=TYPES)
    groups = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True)


class Trip(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    trip_guardian = models.ManyToManyField(Teacher)

#
# class InformationCard(models.Model):
#     pass





