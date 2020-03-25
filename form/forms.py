from django import forms

class CovidForm(forms.ModelForm):
    firstName = forms.CharField()
    lastname = forms.CharField
    question1 = forms.CheckboxInput
    question2 = forms.CheckboxInput
    question3 = forms.CheckboxInput
    question4 = forms.CheckboxInput

    # class Meta:
    #     model = QuestionsForm
    #     fields = all
