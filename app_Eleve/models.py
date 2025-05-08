from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
import random
from django.utils import timezone
from app_User.models import User



class Section(models.Model):
    SECTIONS = (
        (1, "Maternelle"), 
        (2, "Primaire"), 
        (3, "Secondaire")
    )
    nom_section = models.CharField(max_length=100)
    code_section = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return f"{self.nom} ({self.code_section})"


class Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve')
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20, unique=True)
    nom_pere = models.CharField(max_length=100)
    date_inscription = models.DateField(auto_now_add=True)
    nom_mere = models.CharField(max_length=100)
    telephone_pere = models.CharField(max_length=15, unique=True)
    telephone_mere = models.CharField(max_length=15, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='eleves')
   
    def generate_matricule(self):
        # Logique pour générer un matricule unique
        annee = str(self.date_inscription.year)[-2:]
        code_section = self.section.code_section.zfill(2)
        initial_nom = self.nom[0].upper()
        nombre_aleatoire = random(1000, 9999)
        matricule = f"{annee}{code_section}{initial_nom}{nombre_aleatoire}"
        return matricule

    def save(self, *args, **kwargs):
        if not self.matricule:
            self.matricule = self.generate_matricule()
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.user.username} ({self.postnom} {self.matriucule})"
        

