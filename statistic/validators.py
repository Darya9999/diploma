from django import forms
from django.core import validators

def validate_age(value):
    if value < 18 or value > 70:
        raise forms.ValidationError(
            'Возраст некорректный',
            params={'value': value},
        )

def validate_bal(value):
    if value < 2 or value > 5:
        raise forms.ValidationError(
            'Средний балл диплома некорректный',
            params={'value': value},
        )

