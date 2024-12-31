from django import forms


class CompetitionForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    datetime = forms.DateTimeField(label="Date and time", widget=forms.DateTimeInput(attrs={"class": "form-control"}) )