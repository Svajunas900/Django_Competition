from django import forms
from .models import Age, Belt, Weight


class CompetitionForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    datetime = forms.DateTimeField(label="Date and time", widget=forms.DateTimeInput(attrs={"class": "form-control"}) )
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    