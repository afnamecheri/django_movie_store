from django.contrib import admin
from . models import Genre,Movie,Actor,Director


# Register your models here.
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director)



