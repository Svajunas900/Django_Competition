from django.views.generic import TemplateView, FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from .forms import CompetitionForm, CompetitorForm, FilterForm
from .models import (Competition, Weight, Age, Belt, Competitor, 
                     CompetitorLevel, City)
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


class CompetitionView(TemplateView):
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
        age_id = form["age"].value()
        belt_id = form["belt"].value()
        weight_id = form["weight"].value()
        print(age_id, belt_id, weight_id)
        weight = Weight.objects.get(pk=weight_id)
        belt = Belt.objects.get(pk=belt_id)
        age = Age.objects.get(pk=age_id)
        competition = Competition(name=name, date=date_time, age=age, belt=belt, weight=weight)
        competition.save()
        return super().form_valid(form)
    

class RegistrationView(ListView):
    template_name = "registration.html"
    model = Competitor
    form_class = FilterForm
    context_object_name = "competitors"
    paginate_by = 5

    def get_queryset(self):
        queryset = Competitor.objects.all()
        form = FilterForm(self.request.GET)
        if form.is_valid():
            age = form.cleaned_data.get("age")
            belt = form.cleaned_data.get("belt")   
            weight = form.cleaned_data.get("weight")
            if age:
                 queryset = queryset.filter(age=age)
            if belt:
                 queryset = queryset.filter(belt=belt)
            if weight:
                queryset = queryset.filter(weight=weight)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FilterForm(self.request.GET)
        context["is_organizer"] = self.request.user.groups.filter(name="Organizers").exists()
        return context


class CompetitorRegistrationsView(FormView):
    template_name = "competitor_registration.html"
    form_class = CompetitorForm
    success_url = "/"

    def form_valid(self, form):
        name = form["name"].value()
        age_id = form["age"].value()
        level_id = form["level"].value()
        city_id = form["city"].value()
        belt_id = form["belt"].value()
        weight_id = form["weight"].value()
        competition_id = form["competition"].value()
        city = City.objects.get(pk=city_id)
        weight = Weight.objects.get(pk=weight_id)
        belt = Belt.objects.get(pk=belt_id)
        age = Age.objects.get(pk=age_id)
        competition_id = Competition.objects.get(pk=competition_id)
        level = CompetitorLevel.objects.get(pk=level_id)
        competitor = Competitor(name=name, age=age, level=level, city=city, competition=competition_id, belt=belt, weight=weight)
        competitor.save()
        return super().form_valid(form)
    
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