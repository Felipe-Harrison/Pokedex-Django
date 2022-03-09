from django.contrib import admin

from .models import pokemon
# Register your models here.

@admin.register(pokemon)
class PokemonAdmin(admin.ModelAdmin):
    ordering = ('number','name')
    list_display = ("number","name","type1","type2")