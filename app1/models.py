from django.db.models import (Model, ForeignKey, CharField, 
    IntegerField, DateTimeField, CASCADE)

# Create your models here.
class City(Model):
    id = IntegerField(primary_key=True)
    city = CharField(max_length=50)


class Competitor_Level(Model):
    id = IntegerField(primary_key=True)
    level = CharField(max_length=50)

# Note
# Use datetime.datetime in date field
class Competition(Model):
    id = IntegerField(primary_key=True)
    date = DateTimeField()
    name = CharField(max_length=50)


class Competitor(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=50)
    age = IntegerField(max_length=3)
    level = ForeignKey(Competitor_Level, on_delete=CASCADE, to_field=id)
    city = ForeignKey(City, on_delete=CASCADE, to_field=id)
    competition = ForeignKey(Competition, on_delete=CASCADE, to_field=id)


class Brackets(Model):
    id = IntegerField(primary_key=True)
    competitor = ForeignKey(Competitor, on_delete=CASCADE, to_field=id)
    competition = ForeignKey(Competition, on_delete=CASCADE, to_field=id)
    lap = IntegerField(max_length=255)