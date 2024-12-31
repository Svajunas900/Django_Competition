from django.test import TestCase
from .models import City, Competition, Competitor, Competitor_Level, Brackets
# Create your tests here.


class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(id=1, city="New York")
        City.objects.create(id=2, city="London")
    

class CompetitionTestCase(TestCase):
    def setUp(self):
        Competition.objects.create(id=1, date="2024-12-31 10:55:39")
        Competition.objects.create(id=2, date="2024-02-04 13:35:39")
        Competition.objects.create(id=3, date="2024-10-02 12:23:39")
    

class CompetitorLevelTestCase(TestCase):
    def setUp(self):
        Competitor_Level.objects.create(id=1)
        Competitor_Level.objects.create(id=2)
        Competitor_Level.objects.create(id=3)
        

class CompetitorTestCase(TestCase):
    def setUp(self):
        Competitor.objects.create(id=1, name="svajunas", age=24)
        Competitor.objects.create(id=2, name="titas", age=19)
    

class BracketsTestCase(TestCase):
    def setUp(self):
        Brackets.objects.create(id=1)
        Brackets.objects.create(id=2)
        Brackets.objects.create(id=3)