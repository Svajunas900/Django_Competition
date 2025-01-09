from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    competitor = models.OneToOneField(User, on_delete=models.CASCADE)
    fibo_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"""Competitor ID: {self.competitor.id}, 
        fibo_number: {self.fibo_number}"""


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
    name = models.CharField(unique=True, max_length=50)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    end_registration_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"""Date: {self.date.strftime("%Y-%m-%d %H:%M:%S")}, 
        Name: {self.name}, 
        Registration end: {self.end_registration_date.strftime("%Y-%m-%d %H:%M:%S")},
        """


class Competitor(models.Model):
    name = models.CharField(max_length=50)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    level = models.ForeignKey(CompetitorLevel, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)

    def __str__(self):
        return f"""Name: {self.name},
          {self.age}, 
          {self.level}, 
          {self.city}, 
          Competition: {self.competition}, 
          {self.weight}, 
          {self.belt}"""   


class Brackets(models.Model):
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    lap = models.IntegerField()

    def __str__(self):
        return f"""Competitor: {self.competitor}, 
        Competition: {self.competition}, 
        Lap: {self.lap}"""
    

ACTION_CHOICES = {
    "LOGGED_IN": "LOGGED IN",
    "LOOKING_FOR_EVENT": "LOOKING FOR EVENTS",
    "REGISTERED_TO_NEW_EVENT": "REGISTERED_TO_NEW_EVENT",
    "USER_REGISTERED": "USER_REGISTERED"
}


class Logs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(choices=ACTION_CHOICES)
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.user}, Action: {self.action}, Time: {self.time}"


class PaymentMethod(models.Model):
    method = models.CharField(choices={"Crypto": "Crypto",
                                       "VirtualAccount": "VirtualAccount",
                                       "BankCard": "BankCard"})

    def __str__(self):
        return f"{self.method}"


class UserPayment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    date_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"""User: {self.user_id}, 
        Method: {self.payment_method}, 
        Amount: {self.payment_amount}, 
        Time: {self.date_time}"""


