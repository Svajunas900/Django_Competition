from django.urls import path
from .views import (HomePageView, ResultsView, BracketsView, 
                        CompetitionView, RegistrationView, CompetitorRegistrationsView, 
                        CreateCompetitionView, LoginView, RegisterView,
                        CompetitorsView)
from django.contrib.auth.views import LogoutView

app1_urls = [
    path('', HomePageView.as_view(), name="home"),
    path('results', ResultsView.as_view(), name="results"),
    path('brackets', BracketsView.as_view(), name="brackets"),
    path('competition', CompetitionView.as_view(), name="competition"),
    path('registration', RegistrationView.as_view(), name="registration"),
    path('competitor_registration', CompetitorRegistrationsView.as_view(), name="competitor_registration"),
    path('create_competition', CreateCompetitionView.as_view(), name="create_competition"),
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("competitors", CompetitorsView.as_view(), name="competitors")
]