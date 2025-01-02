from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .forms import CompetitionForm
from .models import Competition
import datetime
# Create your views here.


class GroupRequiredMixin(LoginRequiredMixin):
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if self.group_required and not request.user.groups.filter(name=self.group_required).exists():
            return HttpResponseForbidden("You do not have permission to view this page.")
        return super().dispatch(request, *args, **kwargs)


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context


class CompetitionView(GroupRequiredMixin, TemplateView):
    template_name = "competition.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context


class CreateCompetitionView(GroupRequiredMixin, FormView):
    template_name = "create_competition.html"
    group_required = "Organizers"
    form_class = CompetitionForm
    success_url = "/"
    
    def form_valid(self, form):
        name = form["name"].value()
        date_time = form["datetime"].value()
        competition = Competition(name=name, date=date_time)
        competition.save()
        return super().form_valid(form)
    

class RegistrationView(TemplateView):
    template_name = "registration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context


class Competitor_RegistrationsView(TemplateView):
    template_name = "competitor_registration.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context


class BracketsView(TemplateView):
    template_name = "brackets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context
    

class ResultsView(TemplateView):
    template_name = "results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context