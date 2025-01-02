from django.test import TestCase
from .models import (City, Competition, Competitor, CompetitorLevel, Brackets,
                     Age, Belt, Weight)
# Create your tests here.


class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(city="New York")
        City.objects.create(city="London")
    

class CompetitionTestCase(TestCase):
    def setUp(self):
        Competition.objects.create(date="2024-12-31 10:55:39")
        Competition.objects.create(date="2024-02-04 13:35:39")
        Competition.objects.create(date="2024-10-02 12:23:39")
    

class CompetitorLevelTestCase(TestCase):
    def setUp(self):
        CompetitorLevel.objects.create()
        CompetitorLevel.objects.create()
        CompetitorLevel.objects.create()
        

class CompetitorTestCase(TestCase):
    def setUp(self):
        Competitor.objects.create(name="svajunas", age=24)
        Competitor.objects.create(name="titas", age=19)
    

class BracketsTestCase(TestCase):
    def setUp(self):
        Brackets.objects.create()
        Brackets.objects.create()
        Brackets.objects.create()


class WeightTestCase(TestCase):
    def setUp(self):
        Weight.objects.create(weight="50-60")
        Weight.objects.create(weight="60-70")
        Weight.objects.create(weight="70-80")


class AgeTestCase(TestCase):
    def setUp(self):
        Age.objects.create(age="13-18")
        Age.objects.create(age="18-23")
        Age.objects.create(age="23-28")


class BeltTestCase(TestCase):
    def setUp(self):
        Belt.objects.create(belt="White")
        Belt.objects.create(belt="Purple")
        Belt.objects.create(belt="Black")