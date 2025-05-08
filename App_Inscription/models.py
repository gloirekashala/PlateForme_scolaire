from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):
    STATUS = [("actif","actif"),("inactif","inactif")]
    USER_TYPE = (
        (0, 'administrateur'),
        (1, 'promoteur'),
        (2, 'prefet'),
        (3, 'directeur'),
        (4, 'comptable'),
        (5, 'secretaire'),
        (6, 'enseignant'),
        (7, 'eleve'),
    )
    GENRE = [("M", "Masculin"), ("F", "Feminin")]
    username = models.CharField(
        max_length=150, 
        validators=[UnicodeUsernameValidator, ], 
        unique=True
    )
    email = models.EmailField(
        unique=True, 
        verbose_name='Email', 
        max_length=255
    )

    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    genre = models.CharField(max_length=1, choices=GENRE, null=True, blank=True)
    photo = models.ImageField(upload_to='photos_users/', null=True, blank=True)
    telephone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.username} ({self.prenom} {self.postnom})"
    


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