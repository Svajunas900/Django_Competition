from django.db import models

# Create your models here.
class City(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"ID: {self.id}, City: {self.city}"

class Competitor_Level(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=50)

    def __str__(self):
        return f"ID: {self.id}, Level: {self.level}"
# Note
# Use datetime.datetime in date field
class Competition(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"ID: {self.id}, Date: {self.date}, Name: {self.name}"


class Competitor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    level = models.ForeignKey(Competitor_Level, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Level: {self.level}, City: {self.city}, Competition: {self.competition}"   

class Brackets(models.Model):
    id = models.IntegerField(primary_key=True)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    lap = models.IntegerField()

    def __str__(self):
        return f"ID {self.id}, Competitor: {self.competitor}, Competition: {self.competition}, Lap: {self.lap}"