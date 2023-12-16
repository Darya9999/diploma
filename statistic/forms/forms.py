from django import forms

from statistic.models import Stat

class StatForm(forms.ModelForm):

    class Meta:
        model = Stat
        fields = ('name', 'sename', 'surname', 'sud', 'kind_obr','age', 'kind_exp','exp_concurent', 'recomendacii','profdop', 'sredball')
