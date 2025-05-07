from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    adresse = models.TextField()
    photo = models.ImageField(upload_to='photos_users/', null=True, blank=True)
    numero_telephone = models.CharField(max_length=15, unique=True)
    typeUsers = models.CharField(
        max_length=50,
        choices=[
            ('admin', 'Administrateur'),
            ('comptable', 'comptable'),
            ('directeur', 'directeur'),
            ('enseignant', 'enseignant'),
            ('eleve', 'eleve'),
            ('parent', 'parent'),
            ('prefet', 'prefet'),
        ]
    )

    def __str__(self):
        return f"{self.username} ({self.prenom} {self.postnom})"
    

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
    mode_paiement = models.CharField(max_length=50, choices=[('espece', 'Espèce'), ('cheque', 'Chèque'), ('virement', 'Virement')])
    reference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Paiement de {self.eleve.user.username} - {self.date_paiement}"
    
class frais(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='frais')
    type_frais = models.CharField(max_length=50, choices=[('scolarite', 'Scolarité'), ('inscription', 'Inscription'), ('autre', 'Autre')])
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_echeance = models.DateField()
    statut = models.CharField(max_length=20, choices=[('payé', 'Payé'), ('impayé', 'Impayé')])

    def __str__(self):
        return f"Frais de {self.eleve.user.username} - {self.type_frais}"
class section(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.IntegerField()
    classe = models.CharField(max_length=50)
    annee_scolaire = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.classe})"