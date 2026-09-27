from MySQLdb import Date
from django import forms

class DateInput(forms.DateInput):
    input_type = "date"

class CreateNewGoal(forms.Form):
    goal = forms.CharField(max_length=255, label='')
    deadline = forms.DateField(widget=DateInput, label='')

