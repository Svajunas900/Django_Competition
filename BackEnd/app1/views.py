from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"


class CompetitionView(TemplateView):
    pass


class RegistrationView(TemplateView):
    pass


class Competitor_RegistrationsView(TemplateView):
    pass


class BracketsView(TemplateView):
    pass


class ResultsView(TemplateView):
    pass
