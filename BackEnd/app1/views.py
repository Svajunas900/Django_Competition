from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
# Create your views here.


class GroupRequiredMixin(LoginRequiredMixin):
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if self.group_required and not request.user.groups.filter(name=self.group_required).exists():
            return HttpResponseForbidden("You do not have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)


class HomePageView(TemplateView):
    template_name = "index.html"


class CompetitionView(GroupRequiredMixin, TemplateView):
    template_name = "competition.html"
    group_required = "Organizers"



class RegistrationView(TemplateView):
    template_name = "registration.html"


class Competitor_RegistrationsView(TemplateView):
    template_name = "competitor_registration.html"


class BracketsView(TemplateView):
    template_name = "brackets.html"


class ResultsView(TemplateView):
    template_name = "results.html"
