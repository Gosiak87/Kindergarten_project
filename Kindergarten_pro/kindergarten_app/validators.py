from django.forms import ValidationError


def check_number(value):
    if 2013> value or value > 2010:
        raise ValidationError("{} liczba nie jest z zakresu 2010 - 2013".format(value))
