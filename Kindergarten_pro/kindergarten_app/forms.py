from django import forms
from .validators import check_number

class ChildAddForm(forms.Form):
    # class Meta:
    #     model = Child
    #     fields = "__all__"

    KINDERGARTEN_GROUPS = {
        (0, "Nieokreślona"),
        (1, "Grupa Zielona"),
        (2, "Grupa Niebieska"),
    }

    first_name = forms.CharField(label="Pierwsze imię:", max_length=64)
    second_name = forms.CharField(label="Drugie imię:", max_length=64)
    last_name = forms.CharField(label="Nazwisko:", max_length=64)
    year_of_birth = forms.IntegerField(label="Data urodzenia", validators=[check_number])
    group = forms.ChoiceField(choices=KINDERGARTEN_GROUPS, widget=forms.RadioSelect)


