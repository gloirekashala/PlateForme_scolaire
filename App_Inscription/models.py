from django.contrib.auth.models import AbstractUser
from django.db import models
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

class payment(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='paiements')
    date_paiement = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    reference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Paiement de {self.eleve.user.username} - {self.date_paiement}"
    
class frais(models.Model):
    nom_frais = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Frais de {self.eleve.user.username} - {self.type_frais}"
    
class section(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"