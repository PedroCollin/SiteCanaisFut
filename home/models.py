from django.db import models
from django.utils import timezone

# Create your models here.


class TeamMates(models.Model):
        nometeam = models.CharField(max_length=40)
        desc = models.CharField(max_length=50)
        mostrar = models.BooleanField(default=True)
        logo = models.ImageField(blank=True, upload_to="foto/%y/%m/%d/")

        def __str__(self):
            return self.nometeam


class Canais(models.Model):
        link = models.CharField(max_length=50)
        canal = models.CharField(max_length=20)
        data = models.DateTimeField()

        def __str__(self):
            return self.canal


class Jogos(models.Model):
        nometeam = models.ForeignKey(TeamMates,on_delete=models.DO_NOTHING)
        descricaoPartida = models.CharField(max_length=50)
        data = models.DateTimeField()
        mostrar = models.BooleanField(default=True)
        canal = models.ForeignKey(Canais,on_delete=models.DO_NOTHING)

        def __str__(self):
            return self.nometeam
