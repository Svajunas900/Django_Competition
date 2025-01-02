from django.db import models


class Age(models.Model):
    age = models.CharField(max_length=20)

    def __str__(self):
        return f"Age: {self.age}"


class Belt(models.Model):
    belt = models.CharField(max_length=50)

    def __str__(self):
        return f"Belt: {self.belt}"


class Weight(models.Model):
    weight = models.CharField(max_length=50)

    def __str__(self):
        return f"Weight: {self.weight}"


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"City: {self.city}"


class CompetitorLevel(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return f"Level: {self.level}"
    

# Note
# Use datetime.datetime in date field
class Competition(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=50)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)

    def __str__(self):
        return f"Date: {self.date}, Name: {self.name}"


class Competitor(models.Model):
    name = models.CharField(max_length=50)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    level = models.ForeignKey(CompetitorLevel, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}, {self.age}, {self.level}, {self.city}, Competition: {self.competition}, {self.weight}, {self.belt}"   


class Brackets(models.Model):
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    lap = models.IntegerField()

    def __str__(self):
        return f"Competitor: {self.competitor}, Competition: {self.competition}, Lap: {self.lap}"
    





