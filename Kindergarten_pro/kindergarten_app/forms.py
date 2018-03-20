from django import forms

from kindergarten_app.models import Child, Carer, Teacher, Group, Trip


class ChildAddForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ("carers", )


class CarerAddForm(forms.ModelForm):
    class Meta:
        model = Carer
        fields = "__all__"


class GroupAddForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class TeacherAddForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class TripAddForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = "__all__"


