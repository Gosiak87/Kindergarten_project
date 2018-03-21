from django.contrib import admin
from .models import Group, Child, Teacher, Carer, Trip, PresenceList

my_classes = [Group, Child, Teacher, Carer, Trip, PresenceList]

for class_ in my_classes:
    admin.site.register(class_)
#
# admin.site.register(Child)
# admin.site.register(Teacher)
# admin.site.register(Carer)

