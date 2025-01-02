from django.test import TestCase
from .models import City, Competition, Competitor, CompetitorLevel, Brackets
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