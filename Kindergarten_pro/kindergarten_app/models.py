from django.db import models
from django.contrib.auth.models import User
from .validators import check_number

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

    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True)
    carers = models.ManyToManyField(Carer)

    @property
    def name(self):
        return "{} {} {}".format(self.first_name, self.second_name, self.last_name)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=64)


class Teacher(models.Model):
    TYPES = (
        (-1, "nieokreślony"),
        (1, "wychowawca przedszkolny"),
        (2, "pedagog"),
        (3, "psycholog"),
        (4, "pomoc wychowawcy"),
        (5, "nauczyciel przedszkolny"),
    )

    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=10)
    type_of_teacher = models.IntegerField(choices=TYPES)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Trip(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    trip_guardian = models.ManyToManyField(Teacher)

#
# class InformationCard(models.Model):
#     pass





