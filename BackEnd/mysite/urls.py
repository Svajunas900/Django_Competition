"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import (HomePageView, ResultsView, BracketsView, 
                        CompetitionView, RegistrationView, CompetitorRegistrationsView, 
                        CreateCompetitionView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('results', ResultsView.as_view(), name="results"),
    path('brackets', BracketsView.as_view(), name="brackets"),
    path('competition', CompetitionView.as_view(), name="competition"),
    path('registration', RegistrationView.as_view(), name="registration"),
    path('competitor_registration', Competitor_RegistrationsView.as_view(), name="competitor_registration"),
    path('create_competition', CreateCompetitionView.as_view(), name="create_competition"),
]
