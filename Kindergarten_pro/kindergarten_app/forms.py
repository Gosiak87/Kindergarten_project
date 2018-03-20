from django import forms

from kindergarten_app.models import Child, Carer, Teacher

# class ChildAddForm(forms.Form):
class ChildAddForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = "__all__"

    # KINDERGARTEN_GROUPS = {
    #     (0, "Nieokreślona"),
    #     (1, "Grupa Zielona"),
    #     (2, "Grupa Niebieska"),
    # }
    #
    # first_name = forms.CharField(label="Pierwsze imię:", max_length=64)
    # second_name = forms.CharField(label="Drugie imię:", max_length=64)
    # last_name = forms.CharField(label="Nazwisko:", max_length=64)
    # year_of_birth = forms.DateField(label="Rok urodzenia")
    # group = forms.ChoiceField(choices=KINDERGARTEN_GROUPS, widget=forms.RadioSelect)


class CarerAddForm(forms.ModelForm):
    class Meta:
        model = Carer
        fields = "__all__"


# class GroupAddForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = "__all__"

class TeacherAddForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


