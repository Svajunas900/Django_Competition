from django.contrib import admin
from .models import Competition, Competitor, Competitor_Level, City, Brackets, Weight, Age, Belt
# Register your models here.

admin.site.register(Competition)
admin.site.register(Competitor)
admin.site.register(Competitor_Level)
admin.site.register(City)
admin.site.register(Brackets)
admin.site.register(Weight)
admin.site.register(Age)
admin.site.register(Belt)