from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve')
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    classe = models.CharField(max_length=50)
    annee_scolaire = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos_eleves/', null=True, blank=True)
    matricule = models.CharField(max_length=20, unique=True)
    nomdu_pere = models.CharField(max_length=100)
    nomde_mere = models.CharField(max_length=100)
    telephone_pere = models.CharField(max_length=15, unique=True)
    telephone_mere = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return f"{self.user.username} ({self.classe})"
