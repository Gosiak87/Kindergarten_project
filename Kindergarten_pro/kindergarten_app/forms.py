from django import forms
from django.forms.widgets import TextInput

from kindergarten_app.models import Child, Carer, Teacher, Group, Trip, PresenceList


class ChildAddForm(forms.ModelForm):

    class Meta:
        model = Child
        exclude = ("carers", )
        widgets = {
            'date_of_birth': TextInput(attrs={'placeholder': 'YYYY-MM-DD',
                                              'class': 'date'}),
        }


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


class PresenceListForm(forms.ModelForm):
    class Meta:
        model = PresenceList
        fields = "__all__"
        widgets = {
        'day': TextInput(attrs={'CheckboxSelectMultiple': ''}),
    }

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", strip=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
