from django.contrib import admin
from .models import (Competition, Competitor, CompetitorLevel, City, 
                     Brackets, Weight, Age, Belt, UserProfile, Logs,
                     PaymentMethod, UserPayment, FlaskFiles)
# Register your models here.

admin.site.register(Competition)
admin.site.register(Competitor)
admin.site.register(CompetitorLevel)
admin.site.register(City)
admin.site.register(Brackets)
admin.site.register(Weight)
admin.site.register(Age)
admin.site.register(Belt)
admin.site.register(UserProfile)
admin.site.register(Logs)
admin.site.register(PaymentMethod)
admin.site.register(UserPayment)
admin.site.register(FlaskFiles)