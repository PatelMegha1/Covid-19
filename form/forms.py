from django import forms
from .models import CovidModel

Ans_Choice = [('YES', 'YES'), ('No', 'NO')]

class CovidForm(forms.ModelForm):
    question1 = forms.ChoiceField(widget=forms.RadioSelect, choices=Ans_Choice)
    question2 = forms.ChoiceField(widget=forms.RadioSelect, choices=Ans_Choice)
    question3 = forms.ChoiceField(widget=forms.RadioSelect, choices=Ans_Choice)
    question4 = forms.ChoiceField(widget=forms.RadioSelect, choices=Ans_Choice)
    class Meta:
        model = CovidModel
        fields = '__all__'