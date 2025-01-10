from django import forms
from .models import Age, Belt, Weight, Competition, City, CompetitorLevel, PaymentMethod
from captcha.fields import CaptchaField


FORM_SELECT_CLASS = "form-select"


class CompetitionForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    datetime = forms.DateTimeField(label="Date and time", widget=forms.DateTimeInput(attrs={"class": "form-control"}) )
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": FORM_SELECT_CLASS}))
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": FORM_SELECT_CLASS}))
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": FORM_SELECT_CLASS}))
    

class CompetitorForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={"class": "form-control form-item"}))
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": "form-control form-item "}) )
    level = forms.ModelChoiceField(queryset=CompetitorLevel.objects.all(), widget=forms.Select(attrs={"class": "form-select form-item"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={"class": "form-select form-item"}))
    competition = forms.ModelChoiceField(queryset=Competition.objects.all(), widget=forms.Select(attrs={"class": "form-select form-item"}))
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": "form-select form-item"}))
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": "form-select form-item"}))
    payment_method = forms.ModelChoiceField(queryset=PaymentMethod.objects.all(), widget=forms.Select(attrs={"class": "form-select form-item"}))
    amount = forms.FloatField(label="Amount", widget=forms.TextInput(attrs={"class": "form-select form-item"}))

class FilterForm(forms.Form):
    weight = forms.ModelChoiceField(queryset=Weight.objects.all(), widget=forms.Select(attrs={"class": FORM_SELECT_CLASS}), required=False)
    age = forms.ModelChoiceField(queryset=Age.objects.all(), widget=forms.Select(attrs={"class": FORM_SELECT_CLASS}), required=False)
    belt = forms.ModelChoiceField(queryset=Belt.objects.all(), widget=forms.Select(attrs={"class": FORM_SELECT_CLASS}), required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    captcha = CaptchaField()
    