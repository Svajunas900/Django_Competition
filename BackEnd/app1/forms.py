from django import forms
from .models import Age, Belt, Weight, Competition, City, CompetitorLevel


class CompetitionForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    datetime = forms.DateTimeField(label="Date and time", widget=forms.DateTimeInput(attrs={"class": "form-control"}) )
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    

class CompetitorForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": "form-control"}) )
    level = forms.ModelChoiceField(queryset=CompetitorLevel.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    competition = forms.ModelChoiceField(queryset=Competition.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))


class FilterForm(forms.Form):
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": "form-select"}), required=False)
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": "form-select"}), required=False)
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": "form-select"}), required=False)