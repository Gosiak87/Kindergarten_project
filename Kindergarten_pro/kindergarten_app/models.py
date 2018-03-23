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
    second_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=10)
    family_connection = models.IntegerField(choices=CONNECTION, default=-1)

    @property
    def name(self):
        second_name = self.second_name or ""
        return "{} {} {}".format(self.first_name, second_name, self.last_name)

    def __str__(self):
        return self.name


class Child(models.Model):

    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True,
                              related_name="child_set")
    carers = models.ManyToManyField(Carer)

    @property
    def name(self):
        second_name = self.second_name or ""
        return "{} {} {}".format(self.first_name, second_name, self.last_name)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


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
    second_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=10)
    type_of_teacher = models.IntegerField(choices=TYPES)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    @property
    def name(self):
        second_name = self.second_name or ""
        return "{} {} {}".format(self.first_name, second_name, self.last_name)

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    trip_guardians = models.ManyToManyField(Teacher)
    members_of_trip = models.ManyToManyField(Child)

    def __str__(self):
        return self.name


class PresenceList(models.Model):
    children = models.ManyToManyField(Child)
    day = models.DateTimeField()
    group = models.ForeignKey(Group, on_delete=None)  # presencelist.group_set


#
#
# class InformationCard(models.Model):
#     child = models.OneToOneField(Child, on_delete=models.SET_NULL, primary_key=True)
#






