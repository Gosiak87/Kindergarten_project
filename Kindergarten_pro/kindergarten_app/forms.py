from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
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


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", strip=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("User lub haslo niepoprawne")
