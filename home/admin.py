from django.contrib import admin
from .models import TeamMates,Canais,Jogos

# Register your models here.

class DetTeams(admin.ModelAdmin):
    list_display = ('id','nometeam','desc','logo',)
    list_editable = ('desc',)
    list_display_links = ('id',)
    search_fields = ('nometeam',)

admin.site.register(Canais)
admin.site.register(Jogos)
admin.site.register(TeamMates,DetTeams)
